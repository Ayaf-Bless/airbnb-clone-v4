from django import forms
from . import models as room_models

class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere")
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(queryset=room_models.RoomType.objects.all())
