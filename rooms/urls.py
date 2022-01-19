from django.urls import path
from . import views

app_name = "room"

urlpatterns = [path("<int:pk>", views.RoomDetail.as_view(), name="detail")]
