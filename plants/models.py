from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    FREQUENCY = [
        ('REG', 'regularly'),
        ('INF', 'infrequently'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(default='images/icon.png', upload_to='images/')
    text = models.TextField(default='...')
    watering_frequency = models.CharField(max_length=3, choices=FREQUENCY)
    watering_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'owner_id'], name='unique_name'),
        ]

    def __str__(self):
        return self.name
