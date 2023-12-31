from . import views
from django.urls import path

urlpatterns = [
    path("pizza/", views.index, name="index"),
    path('', views.main, name="main"),
    path('api_pizza/', views.api),
]