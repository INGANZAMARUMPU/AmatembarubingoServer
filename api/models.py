from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone

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

class SousColline(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    colline = models.ForeignKey(Colline, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.nom} - {self.colline}"

class Enqueteur(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Localite(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    precision = models.FloatField()

    def __str__(self):
        return f"Lat. {self.latitude}, Long {self.longitude}"

class ReseauDAlimentation(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=16)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.now)
    enqueteur = models.ForeignKey(Enqueteur, on_delete=models.PROTECT)
    localite = models.ForeignKey(Localite, on_delete=models.PROTECT)
    sous_colline = models.ForeignKey(SousColline, on_delete=models.PROTECT)
    gravitaire = models.BooleanField()
    pompage = models.BooleanField()
    lineaire_km = models.FloatField(max_length=8)
    gestionnaire = models.CharField(max_length=32)
    nb_captages = models.IntegerField()
    nb_pompes = models.IntegerField()
    nb_reservoirs = models.IntegerField()
    nb_bornes_fontaines_publiques = models.IntegerField()
    nb_branchements_prives = models.IntegerField()
    nb_menages = models.IntegerField()
    observations = models.CharField(max_length=128)

    def __str__(self):
        return self.nom

class Ibombo(models.Model):
    id = models.BigAutoField(primary_key=True)
    serugo = models.CharField(max_length=32)
    umugende = models.CharField(max_length=32)
    rirakora = models.BooleanField()
    nb_menages = models.IntegerField()
    observations = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = "amabombo"

    def __str__(self):
        return self.serugo

