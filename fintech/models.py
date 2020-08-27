from django.db import models


# Create your models here.

class Stock(models.Model):
    symbol = models.CharField('Symbol', max_length=32, primary_key=True)
    date = models.DateField('Date')
    open = models.PositiveIntegerField('Open')
    high = models.PositiveIntegerField('High')
    Low = models.PositiveIntegerField('Low')
    close = models.PositiveIntegerField('Close')
    adj_close = models.PositiveIntegerField('Adj. close')
    Volume = models.PositiveIntegerField('Volume')


class DJI30(models.Model):
    symbol = models.ForeignKey(Stock, on_delete=models.DO_NOTHING)
