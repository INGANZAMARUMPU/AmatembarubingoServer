from django.db import models
from django.contrib.auth.models import User, Group

def getFullname(user: User):
    full_name = f"{user.first_name} {user.last_name}".strip()
    return full_name or user.username

User.add_to_class("__str__", getFullname)

class GROUPS(models.TextChoices):
    ADMIN = "admin"
    ENQUETEUR = "enqueteur"

print("Chargement des groupes")
for value, key in GROUPS.choices:
    Group.objects.get_or_create(value)

class Province(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.nom}"

class Commune(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.province}"

class Colline(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.commune}"

class Enqueteur(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.CASCADE)

class Fiche(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=32)

class Branchement(models.Model):
    id = models.SmallAutoField(primary_key=True)
    proprietaire = models.CharField(max_length=32)

class Resultat(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    precision = models.FloatField()
    nom = models.CharField(max_length=32)
    fiche = models.ForeignKey(Fiche, on_delete=models.PROTECT)
    branchement = models.ForeignKey(Branchement, on_delete=models.PROTECT)
    source = models.CharField(max_length=32)
    eau_accessible = models.BooleanField()
    nb_menages = models.SmallIntegerField()
    observations = models.CharField(max_length=128)
