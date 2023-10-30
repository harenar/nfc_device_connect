from django.shortcuts import render,HttpResponse
from . import main

# Create your views here.



def index(request):
    return HttpResponse(main.main())