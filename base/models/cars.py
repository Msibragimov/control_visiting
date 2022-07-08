from django.db import models
from django.contrib.auth import get_user_model


OWNER_TYPE = [
    ('ST', 'Staff'),
    ('GT', 'Guest')
]


User = get_user_model()

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=50)
    allowed = models.BooleanField(default=False)
    owner_is = models.CharField(max_length=50, choices=OWNER_TYPE)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner} - {self.number}"
