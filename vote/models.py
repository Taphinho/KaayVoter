from django.db import models

# Create your models here.
class Candidat(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nbrvote = models.IntegerField(default = 0)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"