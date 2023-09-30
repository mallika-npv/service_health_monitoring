from django.db import models

class service(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    time = models.IntegerField(default=0)

class days(models.Model):
    date = models.DateField()
    webs = models.TextField(max_length=255, name="webs")
    dt = models.FloatField(name="dt")
    high_dt = models.BooleanField(name="high_dt")
