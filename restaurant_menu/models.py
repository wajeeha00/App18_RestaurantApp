from django.db import models
from django.contrib.auth.models import User

#left - side is the value that will be stored in the database
#right - side is the value that will be displayed to the user
MEAL_TYPE = [
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
]
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique = True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    meal_type= models.CharField(choices=MEAL_TYPE, max_length=1000)
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
