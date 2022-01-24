from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage

from django.views.generic import ListView, DetailView, View
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


class SearchView(View):
    def get(self, request: HttpRequest):
        country = request.GET.get("country")
        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                bed = form.cleaned_data.get("bed")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                super_host = form.cleaned_data.get("super_host")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country
                if room_type is not None:
                    filter_args["room_type"] = room_type
                if price is not None:
                    filter_args["price__lte"] = price
                if guests is not None:
                    filter_args["guests__gte"] = guests
                if bedrooms is not None:
                    filter_args["bedroom__gte"] = bedrooms
                if bed is not None:
                    filter_args["beds__gte"] = bed
                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True
                if super_host is True:
                    filter_args["host__super_host"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility
                qs = room_models.Room.objects.filter(**filter_args).order_by("created_at")
                paginator = Paginator(qs, 10, orphans=5)
                page = request.GET.get("page", 1)
                rooms = paginator.get_page(page)
                return render(request, "rooms/search.html",
                              {"form": form, "rooms": rooms
                               })
        else:
            form = forms.SearchForm()

            return render(request, "rooms/search.html",
                          {"form": form
                           })
