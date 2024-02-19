
from django.db import models

class UserInput(models.Model):
    user_input = models.CharField(max_length=255)
