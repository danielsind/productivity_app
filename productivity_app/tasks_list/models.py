from django.db import models
from django.contrib.auth import get_user_model
from utils.models import Timestamps

# Create your models here.
class List(Timestamps, models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class ListItem(Timestamps, models.Model):
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
