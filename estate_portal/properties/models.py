from django.db import models
from users.models import User


class Property(models.Model):
    TYPE_CHOICES = [('rent', 'rent'), ('sale', 'sale')]

    title = models.CharField(max_length=255)
    owner = User
    price = models.DecimalField(decimal_places=2, max_digits=10)
    address = models.CharField(max_length=255, default='Unknown')
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    area = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='rent')
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
