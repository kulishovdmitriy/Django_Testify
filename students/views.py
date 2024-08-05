from django.shortcuts import render
from django.http.response import HttpResponse

from students.utils import gen_password, parse_length


# Create your views here.


def hello(request):
    return HttpResponse("Hello from Django!!!")


def get_random(request):
    try:
        length = parse_length(request, 15)
    except Exception as err:
        return HttpResponse(str(err), status_code=400)
    result = gen_password(length)
    return HttpResponse(result)
