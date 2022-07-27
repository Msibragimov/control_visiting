from django.db import models


OWNER_TYPE = [
    ('ST', 'Staff'),
    ('GT', 'Guest')
]


class Car(models.Model):
    owner = models.CharField(max_length=50)
    allowed = models.BooleanField(default=False)
    owner_is = models.CharField(max_length=50, choices=OWNER_TYPE)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner} - {self.number}"
