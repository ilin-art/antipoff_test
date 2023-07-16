import requests
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cadastre
from .serializers import CadastreSerializer


EXTERNAL_SERVER_URL = "http://localhost:8080/process/"

@api_view(['POST'])
def query_view(request):
    cadastre_number = request.data.get('cadastre_number')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')
    try:
        payload = {
            'cadastre_number': cadastre_number,
            'latitude': latitude,
            'longitude': longitude
        }
        response = requests.post(EXTERNAL_SERVER_URL, json=payload)
        response.raise_for_status()
        result = response.json().get('result')
        if response.status_code == 200:
            return Response({'result': result})
        else:
            return Response(response.content, status=response.status_code)
    except requests.exceptions.RequestException as e:
        print(e)
        return Response({'error': response.content}, status=500)

@api_view(['POST'])
def result_view(request):
    query = Cadastre.objects.create(
        cadastre_number = request.data.get('cadastre_number'),
        latitude = request.data.get('latitude'),
        longitude = request.data.get('longitude'),
        result = request.data.get('result')
    )
    serializer = CadastreSerializer(query)
    return Response({'status': 'success', 'query': serializer.data})

@api_view(['GET'])
def ping_view(request):
    try:
        connection.cursor()
        return Response({'status': 'Server is running'})
    except Exception as e:
        return Response({'status': 'Server is not running'}, status=500)
