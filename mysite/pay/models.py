from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    '''Orders'''
    subject = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    total_amount = models.FloatField(default=0)
    trade_no = models.CharField(max_length=64)
    time_create = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Oder`s owner')

    def __str__(self):
        return self.subject


