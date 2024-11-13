from django.urls import path
from . import views

app_name = "flora"
urlpatterns = [
    path("",views.index, name="index"),
    path("n1problem", views.n1problem),
    path("n1solution",views.n1solution),
    path("pagination",views.pagination),
    path("infinite-scroll/", views.infinite_scroll_view, name="infinite_scroll"),
    path("infinite-scroll-data/", views.infinite_scroll_plants, name="infinite_scroll_data"),
]
