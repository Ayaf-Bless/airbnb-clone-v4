from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage

from django.views.generic import ListView, DetailView
from . import models as room_models
from django_countries import countries


class HomeView(ListView):
    model = room_models.Room
    paginate_by = 10
    ordering = "created_at"
    paginate_orphans = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["he"] = "hello"
        return contex


class RoomDetail(DetailView):
    model = room_models.Room


def search(request: HttpRequest):
    city = str.capitalize(request.GET.get("city", "Anywhere"))
    room_types = room_models.RoomType.objects.all()
    return render(request, "rooms/search.html", {"city": city, "countries": countries, "room_types": room_types})
# def room_detail(request: HttpResponse, pk):
#     try:
#         room = room_models.Room.objects.get(pk=int(pk))
#         return render(request, "rooms/detail.html", {"room": room})
#     except room_models.Room.DoesNotExist:
#         raise Http404()

#
# # Create your views here.
# def get_rooms(request: HttpRequest):
#     page = int(request.GET.get("page") or 1)
#     all_rooms = room_models.Room.objects.all()
#     paginator = Paginator(all_rooms, 10, orphans=5)
#     try:
#         rooms = paginator.page(page)
#         return render(request, "rooms/home.html",
#                       context={"rooms": rooms})
#     except EmptyPage:
#         return redirect("/")
#
#     # page_size = 10
#     # limit = page_size * page
#     # page_count = ceil(room_models.Room.objects.count() / page_size)
#     # offset = limit - page_size
#     # all_rooms = room_models.Room.objects.all()[offset:limit]
#     # number = 44
