from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        kakao_id = data.get('kakao_id')
        nickname = data.get('nickname')
        print(kakao_id, " ", nickname)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)