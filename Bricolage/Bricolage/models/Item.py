from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
  name = models.CharField(max_length=180)
  description = models.CharField(max_length=180)
  owner = models.ForeignKey(User)

  quantity = models.IntegerField()
  cost = models.FloatField()



