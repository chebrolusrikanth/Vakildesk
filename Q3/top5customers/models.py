from django.db import models
from datetime import timedelta
from django.utils import timezone

class Order(models.Model):
    customer=models.CharField(max_length=100)
    order_date=models.DateField()
    status=models.CharField(max_length=50,default='completed')
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.customer
