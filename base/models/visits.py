from django.db import models
from django.contrib.auth import get_user_model

from .cars import Car
from .staff import Employee


User = get_user_model()

class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)