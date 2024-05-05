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

class SEXE(models.TextChoices):
    HOMME = "homme"
    FEMME = "femme"

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
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="Nom du réseau AEP (Izina ry'umugende)")
    type = models.CharField(max_length=64, choices=TYPE.choices, verbose_name="Autres types d'ouvrage")
    date = models.DateField(default=timezone.localdate, editable=False)
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "reseaux d'alimentation"

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

class Ibombo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    place = models.CharField(max_length=32, choices=PLACE.choices, verbose_name="Borne fontaine proche de(Ibombo rusangi ryegereye he)")
    identification = models.CharField(max_length=32, verbose_name="Identification de la BORNE FONTAINE(Izina ry'iryo bombo rusangi)")
    umugende = models.CharField(max_length=32, verbose_name="Nom réseau AEP")
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["nb_menages","nb_menages_500"],
            "true":[]
        }'''
    )
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    nb_menages_500 = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "amabombo"

    def __str__(self):
        return self.place

class BranchementPrive(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    place = models.CharField(max_length=32, choices=PLACE.choices, verbose_name="Type de BRANCHEMENT PRIVE (IMIHANA CANKE INYUBAKWA RUSANGI IFISE AMAZI I WABO)")
    nom = models.CharField(max_length=32, verbose_name="Nom/ Le nom du proprietaire/ Abonné")
    umugende = models.CharField(max_length=32, verbose_name="Nom du réseau AEP (Izina ry'umugende ayo mazi yamukako)")
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["avec_eau","nb_menages","nb_menages_500","suffisante"],
            "true":[]
        }'''
    )
    avec_eau = models.BooleanField(default=False, verbose_name="Y'a-t-il de l'eau(Barafise amazi)?")
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    nb_menages_500 = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    suffisante = models.BooleanField(default=False, verbose_name="L'eau est-elle suffisante(amazi arakwiye)?")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Captage(models.Model):
    class SYSTEME(models.TextChoices):
        GRAVITAIRE = "Système gravitaire"
        POMPAGE = "Pompage"

    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    umugende = models.CharField(max_length=32, verbose_name="Nom réseau AEP (Izina ry'umugende ayo mazi yamukako)")
    nom = models.CharField(max_length=32, verbose_name="Nom du captage")
    date = models.DateField(default=timezone.localdate, editable=False)
    systeme = models.CharField(max_length=32, choices=SYSTEME.choices, verbose_name="Système de captage")
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["tarissement","protection","debit"],
            "true":[]
        }'''
    )
    tarissement = models.BooleanField(default=False, verbose_name="Tarissement(Iryo riba rirakama)?")
    protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    debit = models.FloatField(verbose_name="Debit de l'eau du système(nombre de littres par seconde)/amalitiro y'amazi yisuka ku musegonda")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Pompe(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="Nom du réseau (Izina ry'umugende)")
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["debit"],
            "true":[]
        }'''
    )
    debit = models.FloatField(verbose_name="Debit de l'eau du système(nombre de littres par seconde)/amalitiro y'amazi yisuka ku musegonda")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Puit(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="Nom de la sous colline (Izina ry'agacimbiri kimbweko iryo riba)")
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Harakoreshwa",
        help_text='''{
            "false":["coloration","nb_menages","nb_menages_500","tarissement","protection"],
            "true":[]
        }'''
    )
    coloration = models.BooleanField(default=False, verbose_name="Cette eau est-elle colorée (amazi arafise ibara)?")
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    nb_menages_500 = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    tarissement = models.BooleanField(default=False, verbose_name="Tarissement(Iryo riba rirakama)?")
    protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Forage(models.Model):
    class TYPE(models.TextChoices):
        MANUEL = "Manuel"
        ELECTRIQUE = "Éléctrique"
        SOLAIRE = "Solaire"

    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=32, choices=TYPE.choices)
    nom = models.CharField(max_length=32, verbose_name="Nom de la sous colline (Izina ry'agacimbiri kimbweko iryo riba)")
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Harakoreshwa",
        help_text='''{
            "false":["coloration","nb_menages","nb_menages_500","tarissement","protection"],
            "true":[]
        }'''
    )
    coloration = models.BooleanField(default=False)
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    nb_menages_500 = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    tarissement = models.BooleanField(default=False, verbose_name="Tarissement(Iryo riba rirakama)?")
    protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class Reservoir(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="nom du réseau")
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Irakoresha",
        help_text='''{
            "false":["volume"],
            "true":[]
        }'''
    )
    volume = models.FloatField(verbose_name="le volume du réservoir en mettres cube (ubwaguke bw'ikigega)")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom

class SourceAmenagee(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="Nom de la SA(Izina ry'iryo soko)")
    sous_colline = models.CharField(max_length=32, verbose_name="Emplacement de la SA(sous-colline)/ Agacimbiri karimwo iryo soko")
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["coloration","nb_menages","nb_menages_500","tarissement","protection"],
            "true":[]
        }'''
    )
    coloration = models.BooleanField(default=False, verbose_name="Cette eau est-elle colorée (amazi arafise ibara)?")
    tarissement = models.BooleanField(default=False, verbose_name="Tarissement(Iryo riba rirakama)?")
    protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    nb_menages = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    nb_menages_500 = models.PositiveIntegerField(verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "Sources aménagées"

class SourceNonAmenagee(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="Nom de la SNA(Izina ry'iryo soko)")
    fonctionnel = fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["coloration","tarissement","sous_colline"],
            "true":[]
        }'''
    )
    coloration = models.BooleanField(default=False, verbose_name="Cette eau est-elle colorée (amazi arafise ibara)?")
    tarissement = models.BooleanField(default=False, verbose_name="Tarissement(Iryo riba rirakama)?")
    sous_colline = models.CharField(max_length=32, verbose_name="Emplacement de la SA(sous-colline)/ Agacimbiri karimwo iryo soko")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "Sources non-aménagées"

class VillageModerne(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    nom = models.CharField(max_length=32, verbose_name="Nom du village (Izina ry'ikigwati)")
    date = models.DateField(default=timezone.localdate, editable=False)
    fonctionnel = fonctionnel = models.BooleanField(
        default=False, verbose_name="Le village est-il alimenté en eau potable/Ico kigwati kirafise amazi?",
        help_text='''{
            "false":["province","commune","source"],
            "true":["province_a_capter","commune_a_capter","source_a_capter",]
        }'''
    )
    province = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara irimwo isoko ritanga amazi kuri ico kigwati")
    commune = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine irimwo isoko ritanga amazi kuri ico kigwati")
    source = models.CharField(max_length=32, verbose_name="Nom de la source d'eau")
    province_a_capter = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara ihegereye wokurako amazi")
    commune_a_capter = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine ihegereye wokurako amazi")
    source_a_capter = models.CharField(max_length=32, verbose_name="Nom de la source d'eau à capter(isoko rihegereye wokurako amazi)")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "villages modernes"

class VillageCollinaire(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    sexe = models.CharField(max_length=8, choices=SEXE.choices)
    telephone = models.CharField(max_length=12)
    colline = models.ForeignKey(Colline, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    nom = models.CharField(max_length=32, verbose_name="Nom du village (Izina ry'ikigwati)")
    fonctionnel = fonctionnel = models.BooleanField(
        default=False, verbose_name="Le village est-il alimenté en eau potable/Ico kigwati kirafise amazi?",
        help_text='''{
            "false":["province","commune","source"],
            "true":["province_a_capter","commune_a_capter","source_a_capter",]
        }'''
    )
    province = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara irimwo isoko ritanga amazi kuri ico kigwati")
    commune = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine irimwo isoko ritanga amazi kuri ico kigwati")
    source = models.CharField(max_length=32, verbose_name="Nom de la source d'eau")
    province_a_capter = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara ihegereye wokurako amazi")
    commune_a_capter = models.CharField(max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine ihegereye wokurako amazi")
    source_a_capter = models.CharField(max_length=32, verbose_name="Nom de la source d'eau à capter(isoko rihegereye wokurako amazi)")
    observations = models.CharField(max_length=128, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "Villages collinaires"
