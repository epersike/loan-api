import uuid
from datetime import datetime
from django.db import models


# Create your models here.

class Contract(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    qty_payment = models.IntegerField()
    interest_rate = models.DecimalField(decimal_places=2, max_digits=10)
    ip_address = models.CharField(max_length=32)
    ts_subscription = models.DateField(auto_now=False, auto_now_add=True)
    bank_name = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)


class Payment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    payment_original_date = models.DateField(auto_now=False, auto_now_add=False) # When does cpustomer should pay this?p Cont
    payment_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=10) # total_amount / qty_payment - The original amount customer should pay
    total = models.DecimalField(decimal_places=2, max_digits=10, null=True) # subtotal + interest_rate - Total actually paid
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)

    def create(self, *args, **kwargs):
        return super(Payment, self).create(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)
