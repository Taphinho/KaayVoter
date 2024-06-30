from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    NIN = models.CharField(max_length=100)
    dejaVote = models.BooleanField(default=False)
    isauth = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

