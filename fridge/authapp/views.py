import requests
from django.shortcuts import redirect, render
from django.conf import settings

def kakao_login(request):
    kakao_auth_url = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={settings.KAKAO_REST_API_KEY}&redirect_uri={settings.KAKAO_REDIRECT_URI}"
    return redirect(kakao_auth_url)

def kakao_callback(request):
    code = request.GET.get('code')
    token_url = "https://kauth.kakao.com/oauth/token"
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': settings.KAKAO_REST_API_KEY,
        'redirect_uri': settings.KAKAO_REDIRECT_URI,
        'code': code,
    }
    token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    token_response = requests.post(token_url, data=token_data, headers=token_headers)
    token_json = token_response.json()
    access_token = token_json.get('access_token')

    profile_url = "https://kapi.kakao.com/v2/user/me"
    profile_headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    profile_response = requests.get(profile_url, headers=profile_headers)
    profile_json = profile_response.json()

    kakao_id = profile_json.get('id')
    nickname = profile_json.get('properties').get('nickname')

    # 사용자 정보를 사용해 유저를 생성하거나 업데이트하는 로직 추가
    # 예: User 모델을 사용해 유저 생성/업데이트

    return render(request, 'authapp/profile.html', {'nickname': nickname, 'email': email})
