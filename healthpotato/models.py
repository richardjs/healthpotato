from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Data(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    notes = models.TextField(default='', blank=True)

    class Meta:
        abstract = True


class ExerciseData(Data):
    AEROBIC = 0
    ANAEROBIC = 1

    type = models.IntegerField(choices=[
        (AEROBIC, 'Aerobic'),
        (ANAEROBIC, 'Anaerobic'),
    ])
    effort = models.IntegerField(choices=[
        (x, x) for x in range(1, 6)
    ])

    class Meta:
        verbose_name_plural = 'Exercise data'

    def __str__(self):
        return f'exercise {self.user.username} {self.timestamp}'


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
