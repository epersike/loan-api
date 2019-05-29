import uuid
from django.db import models

# Create your models here.

class Contract(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    amount = models.DecimalField(decimal_places=2)
    interest_rate = models.DecimalField(decimal_places=2)
    ip_address = models.CharField(max_length=32)