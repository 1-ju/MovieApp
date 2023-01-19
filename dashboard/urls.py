from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile, name = "profile"),
    path("watchlist/", views.watchlist, name = "watchlist"),
    path("edit/", views.Edit, name="editprofile"),
]