from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def getRoutes(request):
    # safe false to return more than just a python dictionary
    return JsonResponse("Our Api", safe=False)
