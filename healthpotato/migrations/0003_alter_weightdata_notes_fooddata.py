# Generated by Django 4.0a1 on 2021-10-07 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('healthpotato', '0002_weightdata_notes_delete_mealdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightdata',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.CreateModel(
            name='FoodData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('notes', models.TextField(blank=True, default='')),
                ('nutrition', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('amount', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Food data',
            },
        ),
    ]
