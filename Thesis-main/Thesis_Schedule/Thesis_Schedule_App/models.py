from django.db import models

class Item(models.Model):
    fname =  models.CharField(max_length=100)
