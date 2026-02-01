from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    TX_TYPES = (
        ('BUY', 'BUY'),
        ('SELL', 'SELL'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    crypto = models.CharField(max_length = 20)
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)
    tx_type = models.CharField(max_length = 4, choices = TX_TYPES)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.user.username} - {self.tx_type} {self.crypto}"