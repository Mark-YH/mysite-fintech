from django.db import models


# Create your models here.

class Stock(models.Model):
    symbol = models.CharField('Symbol', max_length=32, primary_key=True)
    date = models.DateField('Date')
    open = models.FloatField('Open')
    high = models.FloatField('High')
    low = models.FloatField('Low')
    close = models.FloatField('Close')
    adj_close = models.FloatField('Adj. close')
    volume = models.FloatField('Volume')


class DJI30(models.Model):
    symbol = models.ForeignKey(Stock, on_delete=models.DO_NOTHING)
