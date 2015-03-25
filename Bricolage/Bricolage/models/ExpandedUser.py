from django.db import models
from django.contrib.auth.models import User

class ExpandedUser(models.Model):
  class_year = models.IntegerField()
  owner = models.ForeignKey(User)



