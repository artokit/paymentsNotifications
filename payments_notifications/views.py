from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    print(request.POST)
    return JsonResponse({'message': 'text'})
