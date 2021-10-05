from django.urls import path

from healthpotato import views


urlpatterns = [
    path('', views.home),
    path('weight', views.weight, name="weight-entry"),
]
