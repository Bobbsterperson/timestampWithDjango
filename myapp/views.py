from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import TimestampRecord
from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt
def is_alive(request):
    return JsonResponse({'status': 'alive'})

@csrf_exempt
def timestamp(request):
    if request.method == 'GET':
        randnum = random(1, 2 ,3)
        TimestampRecord.objects.create()
        return JsonResponse({'timestamp': timezone.now()})
    


