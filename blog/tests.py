from django.test import TestCase
from django.http import HttpResponse
# Create your tests here.


def hello_world(request):
    return  HttpResponse("hello world")

