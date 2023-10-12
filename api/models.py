from django.db import models

# Create your models here.
class MbotData(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    battery = models.IntegerField()
    sensor_state = models.JSONField()
    humidity = models.FloatField()
