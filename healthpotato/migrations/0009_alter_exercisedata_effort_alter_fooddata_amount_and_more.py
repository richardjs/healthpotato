# Generated by Django 4.0b1 on 2021-11-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthpotato', '0008_alter_weightdata_clothing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisedata',
            name='effort',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
        migrations.AlterField(
            model_name='fooddata',
            name='amount',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
        migrations.AlterField(
            model_name='fooddata',
            name='nutrition',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
    ]