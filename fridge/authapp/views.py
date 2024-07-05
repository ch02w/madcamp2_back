from django.http import JsonResponse
from rest_framework.decorators import api_view
from allauth.socialaccount.models import SocialApp, SocialToken, SocialAccount
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.helpers import complete_social_login
from django.contrib.auth import login
import requests

@api_view(['POST'])
def kakao_login(request):
    access_token = request.data.get('accessToken')
    if access_token is None:
        return JsonResponse({'error': 'Access token is required'}, status=400)

    try:
        # 카카오 API를 통해 사용자 정보 요청
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        kakao_response = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers)
        kakao_profile = kakao_response.json()

        # 사용자 정보가 없는 경우
        if 'id' not in kakao_profile:
            return JsonResponse({'error': 'Invalid token'}, status=400)

        # 사용자 정보 생성
        kakao_id = kakao_profile['id']
        email = kakao_profile.get('kakao_account', {}).get('email', '')

        # 소셜 어카운트 생성 및 로그인 처리
        app = SocialApp.objects.get(provider='kakao')
        token = SocialToken(token=access_token, app=app)
        token.save()

        account, created = SocialAccount.objects.get_or_create(uid=kakao_id, provider='kakao', defaults={'extra_data': kakao_profile})
        if not created:
            account.extra_data = kakao_profile
            account.save()

        # 소셜 로그인 완료
        complete_social_login(request._request, account)
        login(request._request, account.user)

        return JsonResponse({'isSuccess': True})
    except Exception as e:
        return JsonResponse({'isSuccess': False, 'error': str(e)}, status=500)
