from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from healthpotato.forms import FoodDataForm, WeightDataForm


@login_required
def home(request):
    return render(request, 'healthpotato/home.html')


@login_required
def food(request):
    if request.method == 'POST':
        form = FoodDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.timestamp = timezone.now()
            data.save()

            return HttpResponseRedirect(reverse(home))

    else:
        form = FoodDataForm()

    return render(request, 'healthpotato/food.html', locals())


@login_required
def weight(request):
    if request.method == 'POST':
        form = WeightDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.timestamp = timezone.now()
            data.save()

            return HttpResponseRedirect(reverse(home))

    else:
        form = WeightDataForm()

    return render(request, 'healthpotato/weight.html', locals())
