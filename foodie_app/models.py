from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone



class Ramen(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=200)
    RAMEN_TYPE = [
        (1, "shoyu"),
        (2, "miso"),
        (3, "tonkotsu")
    ]
    ramenType = models.IntegerField(choices=RAMEN_TYPE)
    shop = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    TYPICAL_MEAL_TIME = [
        (1, "morning"),
        (2, "afternoon"),
        (3, "evening")
    ]
    typicalMealTime = models.IntegerField(choices=TYPICAL_MEAL_TIME)
    dateAdded = models.DateTimeField(default=timezone.now)
    avgRating = models.FloatField(default=0)
    numberOfVotes = models.IntegerField(default=0)

class MealRating(models.Model):
    ramen = models.ForeignKey(Ramen, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    dateOfRating = models.DateTimeField(default=timezone.now)
