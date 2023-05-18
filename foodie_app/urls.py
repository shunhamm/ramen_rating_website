from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shoyu/", views.shoyu_ramen, name="shoyu"),
    path("miso/", views.miso_ramen, name="miso"),
    path("tonkotsu", views.tonkotsu_ramen, name="tonkotsu"),
    path("recently_added", views.recently_added, name="recently_added"),
    path("top_rated", views.top_rated, name="top_rated"),
    path("ramen_detail", views.ramen_detail, name="ramen_detail"),
    path("submit_ramen", views.submit_ramen, name="submit_ramen")
]
