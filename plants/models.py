from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
    FREQUENCY = [
        ('REG', 'regularly'),
        ('INF', 'infrequently'),
    ]
    name = models.CharField(max_length=100, unique=True)
    text = models.TextField(default='...')
    watering_frequency = models.CharField(max_length=3, choices=FREQUENCY)
    watering_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name