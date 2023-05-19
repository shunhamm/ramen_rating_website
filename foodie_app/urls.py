from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/ramen_type/<str:ramen_type>/", views.ramen_type_view, name="category"),
    path("category/recently_added/", views.recently_added_view, name="recently_added"),
    path("category/top_rated/", views.top_rated_view, name="top_rated"),
    # path("ramen_detail/", views.ramen_detail_view(), name="ramen_detail"),
    path("submit_ramen/", views.submit_ramen, name="submit_ramen")
]
