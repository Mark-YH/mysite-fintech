from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def test(request):
    if request.method == 'GET':
        context = {
            "version1": {
                "training": {
                    "Y2Y": {

                    },
                    "Y2H": {

                    },
                    "Y2Q": {

                    }
                },
                "testing": {
                    "Y2Y": {

                    },
                    "Y2H": {

                    },
                    "Y2Q": {

                    }
                },
                "params": {
                    "population": 10,
                    "generation": 10000,
                    "theta": 0.004,
                    "init fund": 1e7,
                    "encoding bit": 7
                }
            },
            "version2": {
                "training": {
                    "Y2Y": {
                        "periods": [

                        ],
                        "execution time": 123
                    },
                    "Y2H": {

                    },
                    "Y2Q": {

                    }
                },
                "testing": {
                    "Y2Y": {

                    },
                    "Y2H": {

                    },
                    "Y2Q": {

                    }
                },
                "params": {
                    "population": 10,
                    "generation": 10000,
                    "theta": 0.004,
                    "init fund": 1e7,
                    "encoding bit": 7
                }
            }
        }
        return JsonResponse(context)
