from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')

def hack(request):
    return HttpResponse('Ya vas vzlomal')