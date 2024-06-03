from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import TimestampRecord
from django.views.decorators.csrf import csrf_exempt
import random
import json
from django.core.validators import validate_slug
from django.core.exceptions import ValidationError
from pydantic import BaseModel, Field, ValidationError

@csrf_exempt
def is_alive(request):
    return JsonResponse({'status': 'alive'})

class NameAgeModel(BaseModel):
    name: str = Field(..., pattern="^[a-zA-Z]+$", description="name must be letters")
    age: int

@csrf_exempt
def name_age(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        validated_data = NameAgeModel(**data)
        return JsonResponse({'name': validated_data.name, 'age': validated_data.age}, status=200)
    

@csrf_exempt
def timestamp(request):
    if request.method == 'GET':
        try:
            region = random.randint(1, 3)
            region_db = f"region{region}"
            timestamp_record = TimestampRecord.objects.using(region_db).create(region=region)
            response_data = {
                'timestamp': timestamp_record.timestamp,
                'region': timestamp_record.region
            }

            
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    # elif request.method == 'POST':
    #     try:
    #         data = request.POST
    #         name = data.get('name')
    #         age = data.get('age')
            
    #         if not isinstance(name, str):
    #             return JsonResponse({'error': 'Name must be a string'}, status=400)
            
    #         try:
    #             age = int(age)
    #         except ValueError:
    #             return JsonResponse({'error': 'Age must be an integer'}, status=400)

    #         return JsonResponse({'message': 'Data validated successfully'}, status=200)
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)}, status=500)