from django.urls import include, path

from healthpotato import views


urlpatterns = [
    path('', views.home),
    path('food', views.food, name="food-entry"),
    path('weight', views.weight, name="weight-entry"),

    path('accounts/', include('django.contrib.auth.urls')),
]
