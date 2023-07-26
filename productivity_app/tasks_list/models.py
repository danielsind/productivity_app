from django.db import models
from django.contrib.auth import get_user_model
from utils.models import Timestamps

# Create your models here.
class List(Timestamps, models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
