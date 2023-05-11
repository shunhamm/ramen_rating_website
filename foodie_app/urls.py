from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.shoyu_ramen, name="shoyu"),
    path("", views.miso_ramen, name="miso"),
    path("", views.tonkotsu_ramen, name="tonkotsu"),
    path("", views.recently_added, name="recently_added"),
    path("", views.top_rated, name="top_rated"),
    path("", views.ramen_detail, name="ramen_detail"),
    path("", views.submit_ramen, name="submit_ramen")
]
