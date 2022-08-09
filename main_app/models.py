from operator import mod
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Watch(models.Model):
  brand = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  reference = models.CharField(max_length=100)
  delivery = models.CharField(max_length=100)
  year = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.brand

  def get_absolute_url(self):
      return reverse("watches_detail", kwargs={"watch_id": self.id})
  