from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def test(request):
    if request.method == 'GET':
        context = {
            "AAPL": {
                "2020/1/2": 100,
                "2020/1/3": 110,
                "2020/1/4": 120,
                "2020/1/5": 130,
                "2020/1/6": 120,
                "2020/1/7": 110,
                "2020/1/8": 100,
                "2020/1/9": 120,
                "2020/1/10": 110
            }
        }
        return JsonResponse(context)
