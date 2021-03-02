import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello World. First Django Project. PythonCircle.Com")


@csrf_exempt
def index2(request):
    if request.method == "POST":
        d = {'dict': 1, 'dictionary': 2}
        return HttpResponse(json.dumps(d))

    return HttpResponse("Hello World. First Django Project. PythonCircle.Com")
