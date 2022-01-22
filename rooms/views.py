from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage

from django.views.generic import ListView, DetailView
from . import models as room_models, forms
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
    # city = str.capitalize(request.GET.get("city", "Anywhere"))
    # country = request.GET.get("country", "AF")
    # room_type = int(request.GET.get("room_types", 0))
    # price = int(request.GET.get("price", 0))
    # guests = int(request.GET.get("guests", 0))
    # bedroom = int(request.GET.get("bedroom", 0))
    # beds = int(request.GET.get("beds", 0))
    # baths = int(request.GET.get("baths", 0))
    # s_amenities = request.GET.getlist("amenities")
    # s_facilities = request.GET.getlist("facilities")
    # instant = bool(request.GET.get("instant", False))
    # super_host = bool(request.GET.get("super_host", False))
    #
    # form = {"city": city,
    #         "room_type": room_type,
    #         "country": country,
    #         "price": price,
    #         "guests": guests,
    #         "bedroom": bedroom,
    #         "beds": beds,
    #         "baths": baths,
    #         "s_amenities": s_amenities,
    #         "s_facilities": s_facilities,
    #         "instant": instant,
    #         "super_host": super_host,
    #         }
    #
    # room_types = room_models.RoomType.objects.all()
    # amenities = room_models.Amenity.objects.all()
    # facilities = room_models.Facility.objects.all()
    #
    # choices = {"countries": countries,
    #            "room_types": room_types, "amenities": amenities,
    #            "facilities": facilities,
    #            }
    #
    # filter_args = {}
    #
    # if city != "Anywhere":
    #     filter_args["city__startswith"] = city
    #
    # filter_args["country"] = country
    # if room_type != 0:
    #     filter_args["room_type__pk"] = room_type
    # if price != 0:
    #     filter_args["price__lte"] = price
    # if guests != 0:
    #     filter_args["guests__gte"] = guests
    # if bedroom != 0:
    #     filter_args["bedroom__gte"] = bedroom
    # if beds != 0:
    #     filter_args["beds__gte"] = beds
    # if baths != 0:
    #     filter_args["baths__gte"] = baths
    #
    # if instant is True:
    #     filter_args["instant_book"] = True
    # if super_host is True:
    #     filter_args["host__super_host"] = True
    #
    # if len(s_amenities) > 0:
    #     for s_amenity in s_amenities:
    #         filter_args["amenities__pk"] = int(s_amenity)
    #
    # if len(s_facilities) > 0:
    #     for s_facility in s_facilities:
    #         filter_args["amenities__pk"] = int(s_facility)
    #
    # rooms = room_models.Room.objects.filter(**filter_args)
    form = forms.SearchForm()
    return render(request, "rooms/search.html",
                  {"form": form,
                   })
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
