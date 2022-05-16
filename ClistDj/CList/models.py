from django.db import models

# Create your models here.
class Crypto_Curr(models.Model):
    name = models.CharField(max_length=32)
    symbol = models.CharField(max_length=12)
    avg_price = models.FloatField(null=True, blank= True)
    binance_price = models.FloatField()
    binance_maxPrice = models.FloatField()
    FTX_price = models.FloatField()
    FTX_maxPrice = models.FloatField()
    Kraken_price = models.FloatField()
    Kraken_maxPrice = models.FloatField()
    GateIo_price = models.FloatField()
    GateIo_maxPrice = models.FloatField()

    def clean(self):
        self.avg_price = (self.binance_price + self.Kraken_price + self.GateIo_price + self.FTX_price) / 4
        self.save()