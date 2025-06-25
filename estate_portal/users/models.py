from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.email})"