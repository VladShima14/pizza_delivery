from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    favourite_pizza = models.ForeignKey(
        'pizza_app.PizzaMenuItem', null=True, default=None, blank=True)
    our_note = models.CharField(max_length=140, blank=True)
