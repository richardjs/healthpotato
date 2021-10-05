from django.urls import include, path

from healthpotato import views


urlpatterns = [
    path('', views.home),
    path('weight', views.weight, name="weight-entry"),

    path('accounts/', include('django.contrib.auth.urls')),
]
