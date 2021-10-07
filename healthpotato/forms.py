from django.forms import ModelForm

from healthpotato.models import FoodData, WeightData


class FoodDataForm(ModelForm):
    class Meta:
        model = FoodData
        fields = ['nutrition', 'amount', 'notes']


class WeightDataForm(ModelForm):
    class Meta:
        model = WeightData
        fields = ['weight', 'notes']
