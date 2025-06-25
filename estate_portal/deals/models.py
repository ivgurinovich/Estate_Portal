from django.db import models
from users.models import User
from properties.models import Property


class Deal(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.buyer.name} - {self.property.title}"