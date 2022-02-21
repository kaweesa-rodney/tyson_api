from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Bank_transactions(models.Model):
    entry_user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    tran_id = models.CharField(max_length=10)
    amount = models.IntegerField()
    entry_date = models.DateTimeField(default=datetime.now)
    payment_method = models.CharField(max_length=25)
