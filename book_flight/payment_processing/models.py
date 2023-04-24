from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.model):
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=)