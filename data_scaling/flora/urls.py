from django.urls import path
from . import views

app_name = "flora"
urlpatterns = [
    path("",views.index, name="index"),
    path("n1problem", views.n1problem)
]
