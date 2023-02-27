from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
