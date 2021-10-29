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


class EntryView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy(home)
    initial = {'timestamp': timezone.now,}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExerciseEntryView(EntryView):
    model = ExerciseData
    fields = ['type', 'effort', 'notes', 'timestamp',]


class FoodEntryView(EntryView):
    model = FoodData
    fields = ['nutrition', 'amount', 'notes', 'timestamp',]


class WeightEntryView(EntryView):
    model = WeightData
    fields = ['weight', 'clothing',  'notes', 'timestamp',]
