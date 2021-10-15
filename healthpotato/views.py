from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit  import CreateView

from healthpotato.models import ExerciseData, FoodData, WeightData


@login_required
def home(request):
    return render(request, 'healthpotato/home.html')


class ExerciseEntryView(LoginRequiredMixin, CreateView):
    model = ExerciseData
    fields = ['type', 'effort', 'notes']
    success_url = reverse_lazy(home)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.timestamp = timezone.now()
        return super().form_valid(form)


class FoodEntryView(LoginRequiredMixin, CreateView):
    model = FoodData
    fields = ['nutrition', 'amount', 'notes']
    success_url = reverse_lazy(home)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.timestamp = timezone.now()
        return super().form_valid(form)


class WeightEntryView(LoginRequiredMixin, CreateView):
    model = WeightData
    fields = ['weight', 'notes']
    success_url = reverse_lazy(home)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.timestamp = timezone.now()
        return super().form_valid(form)
