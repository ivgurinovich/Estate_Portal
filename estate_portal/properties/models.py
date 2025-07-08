from django.db import models
from users.models import User


class Property(models.Model):
    TYPE_CHOICES = [('rent', 'rent'), ('sale', 'sale')]

    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
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


class DealRequest(models.Model):
    STATUSES = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    seeker = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES)

    def __str__(self):
        return f"Deal Request for {self.id} for {self.property.title}"