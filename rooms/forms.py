from django import forms
from . import models as room_models
from django_countries.fields import CountryField


class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="UG").formfield()
    room_type = forms.ModelChoiceField(
        queryset=room_models.RoomType.objects.all(),
        empty_label="Any kind",
        required=False)
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    bed = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    super_host = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(queryset=room_models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple())
    facilities = forms.ModelMultipleChoiceField(queryset=room_models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple())
