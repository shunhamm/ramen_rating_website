# Generated by Django 4.2 on 2023-04-25 08:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('imageUrl', models.CharField(max_length=200)),
                ('countryOfOrigin', models.CharField(max_length=200)),
                ('typicalMealTime', models.IntegerField(choices=[(1, 'morning'), (2, 'afternoon'), (3, 'evening')])),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('avgRating', models.FloatField(default=0)),
                ('numberOfVotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MealRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('dateOfRating', models.DateTimeField(default=django.utils.timezone.now)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie_app.meal')),
            ],
        ),
    ]