from django.db import models
from utils.models import Timestamps

# Create your models here.
class List(Timestamps, models.Model):
    user_id = models.ForeignKey(User, )
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
