from django.contrib.auth.models import User
from django.db import models


class Data(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    notes = models.TextField(default='', blank=True)

    class Meta:
        abstract = True


class FoodData(Data):
    nutrition = models.IntegerField(choices=[
        (x, x) for x in range(1, 6)
    ])
    amount = models.IntegerField(choices=[
        (x, x) for x in range(1, 6)
    ])

    class Meta:
        verbose_name_plural = 'Food data'

    def __str__(self):
        return f'food {self.user.username} {self.timestamp}'


class WeightData(Data):
    weight = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        verbose_name_plural = 'Weight data'

    def __str__(self):
        return f'weight {self.user.username} {self.timestamp}'
