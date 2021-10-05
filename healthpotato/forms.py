from django.forms import ModelForm

from healthpotato.models import WeightData


class WeightDataForm(ModelForm):
    class Meta:
        model = WeightData
        fields = ['weight', 'notes']
