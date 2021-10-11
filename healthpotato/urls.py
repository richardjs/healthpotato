from django.urls import include, path

from healthpotato import views


urlpatterns = [
    path('', views.home, name='home'),
    path('exercise', views.ExerciseEntryView.as_view(), name='exercise-entry'),
    path('food', views.FoodEntryView.as_view(), name='food-entry'),
    path('weight', views.WeightEntryView.as_view(), name='weight-entry'),

    path('accounts/', include('django.contrib.auth.urls')),
]
