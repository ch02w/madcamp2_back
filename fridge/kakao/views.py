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

        user, created = User.objects.get_or_create(
            kakao_id=kakao_id,
            defaults={'nickname': nickname}
        )

        if not created:
            user.nickname = nickname
            user.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)