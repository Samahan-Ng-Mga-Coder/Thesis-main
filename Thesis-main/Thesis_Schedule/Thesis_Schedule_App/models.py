from django.db import models


class Rank(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Professor(models.Model):
    id_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    suffix_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    birthday = models.CharField(max_length=10)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    age = models.CharField(max_length=5)
    status = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
