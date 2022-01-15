from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def all_rooms(request: HttpRequest):
    return render(request,"all_rooms")
