from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage

from django.views.generic import ListView
from . import models as room_models


class HomeView(ListView):
    model = room_models.Room
    paginate_by = 10
    ordering = "created_at"
    paginate_orphans = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["he"] = "hello"
        return contex


def room_detail(request: HttpResponse, pk):
    print(pk)
    return render(request, "rooms/detail.html")

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
