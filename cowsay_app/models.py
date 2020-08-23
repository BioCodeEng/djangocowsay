from django.db import models
import subprocess

# Create your models here.
class CowText(models.Model):
    text = models.TextField(max_length=135)



