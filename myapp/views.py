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
        try:
            region = random.randint(1, 3)
            timestamp_record = TimestampRecord.objects.create(region=region)
            response_data = {
                'timestamp': timestamp_record.timestamp,
                'region': timestamp_record.region
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
