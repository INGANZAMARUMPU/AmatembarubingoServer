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
    try:
        Group.objects.get_or_create(name=value)
    except: continue

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

class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.commune}"

class Colline(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.zone}"

class Enqueteur(models.Model):
    class SEXE(models.TextChoices):
        HOMME = "homme"
        FEMME = "femme"

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)

class ReseauDAlimentation(models.Model):
    class TYPE(models.TextChoices):
        DEPART = "chambre départ"
        COLLECTRICE = "chambre collectrice"
        EQUILIBRE = "chambre d'équilibre"
        VENTOUSE = "chambre de ventouse"
        VANNE_DE_SELECTIONNEMENT = "chambre de vanne de selectionnement"
        COLORATION = "chambre de coloration"
        AERATION = "chambre d'aeration"
        PURGE = "chambre de purge"

    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=16)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    type = models.CharField(max_length=64, choices=TYPE.choices)
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "reseaux d'alimentation"

class Ibombo(models.Model):
    class PLACE(models.TextChoices):
        MENAGE = "menage"
        EGLISE_MOSQUEE = "Eglise/Mosquée"
        ETABLISSEMENT_SCOLAIRE = "Etablissement Scolaire"
        INSTITUTION_PUBLIQUE = "Institution Publique"
        INSTITUTION_PRIVEE = "Institution Privee"
        CDS = "CDS"
        HOPITAL = "Hôpital"
        MARCHE = "Marché"
        AUTRES = "Autres"

    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    place = models.CharField(max_length=32, choices=PLACE.choices)
    identification = models.CharField(max_length=32, verbose_name="Izina ry'iryo bombo rusangi")
    umugende = models.CharField(max_length=32)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Rirakora")
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages(igitigiri c'imihana ihavoma)")
    nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="Nombre de menage à plus de 500m")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "amabombo"

    def __str__(self):
        return self.nom

class BranchementPrive(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="izina serugo canke ry'inyubakwa rusangi")
    umugende = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Rirakora")
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages(igitigiri c'imihana ihavoma)")
    nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="Nombre de menage à plus de 500m")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Captage(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=32)
    code_reseau = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    tarissement = models.BooleanField(default=False)
    protection = models.BooleanField(default=False)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Rirakora")
    debit = models.FloatField(verbose_name="nombre de littres par seconde")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Pompe(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=32)
    code_reseau = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Rirakora")
    debit = models.FloatField(verbose_name="nombre de littres par seconde")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Puit(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nature = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date_forage = models.DateField()
    date = models.DateField(default=timezone.localdate, editable=False)
    coloration = models.BooleanField(default=False)
    protection = models.BooleanField(default=False)
    tarissement = models.BooleanField(default=False)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Harakoreshwa")
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages(igitigiri c'imihana ihavoma)")
    nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="Nombre de menage à plus de 500m")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Forage(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nature = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date_forage = models.DateField()
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Harakoreshwa")
    coloration = models.BooleanField(default=False)
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages(igitigiri c'imihana ihavoma)")
    nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="Nombre de menage à plus de 500m")
    tarissement = models.BooleanField(default=False)
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Reservoir(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    code_reservoir = models.CharField(max_length=32)
    code_reseau = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Kirakora")
    volume = models.FloatField(verbose_name="le volume en mettres cube")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class SourceAmenagee(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    coloration = models.BooleanField(default=False)
    protection = models.BooleanField(default=False)
    tarissement = models.BooleanField(default=False)
    fonctionnel = models.BooleanField(default=False, verbose_name="Fonctionnel / Rirakora")
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages(igitigiri c'imihana ihavoma)")
    nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="Nombre de menage à plus de 500m")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "Sources aménagées"

class SourceNonAmenagee(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    coloration = models.BooleanField(default=False)
    tarissement = models.BooleanField(default=False)
    debit = models.FloatField()
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "Sources non-aménagées"

class VillageModerne(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    alimentation_potable = models.BooleanField(default=False)
    source_a_capter = models.CharField(max_length=32)
    debit = models.FloatField()
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "villages modernes"

class VillageCollinaire(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueteur = models.ForeignKey(Enqueteur, editable=False, null=True, on_delete=models.PROTECT)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=32)
    nom = models.CharField(max_length=32)
    date = models.DateField(default=timezone.localdate, editable=False)
    alimentation_potable = models.BooleanField(default=False)
    source_a_capter = models.CharField(max_length=32)
    debit = models.FloatField()
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "villages collinaires"
