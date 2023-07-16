from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
import random
import time


@csrf_exempt
def process_request(request):
    if request.method == 'POST':
        try:
            body = request.body.decode('utf-8')
            data = json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return HttpResponseBadRequest('Invalid JSON data')
        cadastre_number = data.get('cadastre_number')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        if not cadastre_number or not latitude or not longitude:
            return HttpResponseBadRequest(
                'Missing required data: "cadastre_number", "latitude", "longitude"'
            )
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            return HttpResponseBadRequest('Invalid latitude or longitude')

        result = latitude + longitude > 0
        pause_time = random.randint(1, 60)
        time.sleep(pause_time)
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
