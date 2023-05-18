from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone



class Ramen(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=200)
    RAMEN_TYPE = [
        ("shoyu", "Shoyu"),
        ("miso", "Miso"),
        ("tonkotsu", "Tonkotsu")
    ]
    ramenType = models.CharField(max_length=10, choices=RAMEN_TYPE)
    shop = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    TYPICAL_MEAL_TIME = [
        ("morning", "Morning"),
        ("Afternoon", "Afternoon"),
        ("evening", "Evening")
    ]
    typicalMealTime = models.CharField(max_length=10, choices=TYPICAL_MEAL_TIME)
    dateAdded = models.DateTimeField(default=timezone.now)
    avgRating = models.FloatField(default=0)
    numberOfVotes = models.IntegerField(default=0)

    def __str__(self):
        return self.shop

class MealRating(models.Model):
    ramen_id = models.ForeignKey(Ramen, on_delete=models.CASCADE, default=1)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    dateOfRating = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ramen_id
