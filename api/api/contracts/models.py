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

    def save(self, *args, **kwargs):

        import pdb; pdb.set_trace()

        super(Contract, self).save(*args, **kwargs)

        payment_date = datetime.now()

        for i in range(self.qty_payment):

            # Calculate the due date of the payment
            if payment_date.month == 12:
                payment_date = datetime(payment_date.year+1, 1, payment_date.day)
            else:
                payment_date = datetime(payment_date.year, payment_date.month+1, payment_date.day)

            # construct the payments:
            payment_data = {
                'payment_original_date': payment_date,
                'subtotal' : self.total_amount / self.qty_payment,
                'contract' : self,
            }

            # serialize it
            p = Payment(**payment_data)

            p.save()
            # TODO: payment.payment_date should not be required...


class Payment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    payment_original_date = models.DateField(auto_now=False, auto_now_add=False) # When does cpustomer should pay this?p Cont
    payment_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=10) # total_amount / qty_payment - The original amount customer should pay
    total = models.DecimalField(decimal_places=2, max_digits=10, blank=True) # subtotal + interest_rate - Total actually paid
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):

        super(Payment, self).save(*args, **kwargs)
