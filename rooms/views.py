from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import models as room_models


# Create your views here.
def get_rooms(request: HttpRequest): 
    all_rooms = room_models.Room.objects.all()
    number = 44
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
