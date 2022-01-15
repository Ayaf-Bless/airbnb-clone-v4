from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import models as room_models


# Create your views here.
def get_rooms(request: HttpRequest):
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = room_models.Room.objects.all()[offset:limit]
    number = 44
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
