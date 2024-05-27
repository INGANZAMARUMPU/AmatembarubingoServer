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

class MILIEU(models.TextChoices):
    RURAL = "rural"
    URBAIN = "urbain"

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

print("Chargement des groupes")
for value, key in GROUPS.choices:
    try:
        Group.objects.get_or_create(name=value)
    except: continue

class Province(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=16)

    def __str__(self):
        return self.nom

class Commune(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Colline(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=16)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

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
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    XV_1_nomination = models.CharField(max_length=128, verbose_name="Nom du réseau AEP (Izina ry'umugende)")
    XV_2_type = models.CharField(max_length=64, choices=TYPE.choices, verbose_name="Autres types d'ouvrage")
    XV_4_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "reseaux d'alimentation"

class Ibombo(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    IV_1_place = models.CharField(max_length=32, choices=PLACE.choices, verbose_name="Borne fontaine proche de(Ibombo rusangi ryegereye he)")
    IV_2_identification = models.CharField(max_length=64, verbose_name="Identification de la BORNE FONTAINE(Izina ry'iryo bombo rusangi)")
    IV_3_umugende = models.CharField(max_length=64, verbose_name="Nom réseau AEP")
    IV_4_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["IV_5_nb_menages","IV_6_nb_menages_500"],
            "true":[]
        }'''
    )
    IV_5_nb_menages = models.PositiveIntegerField(null=True, verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    IV_6_nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    IV_7_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "amabombo"

class BranchementPrive(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    V_1_place = models.CharField(max_length=32, choices=PLACE.choices, verbose_name="Type de BRANCHEMENT PRIVE (IMIHANA CANKE INYUBAKWA RUSANGI IFISE AMAZI I WABO)")
    V_2_nomination = models.CharField(max_length=128, verbose_name="Nom/ Le nom du proprietaire/ Abonné")
    V_3_umugende = models.CharField(max_length=64, verbose_name="Nom du réseau AEP (Izina ry'umugende ayo mazi yamukako)")
    V_4_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["V_5_avec_eau","V_6_nb_menages","V_7_nb_menages_500","V_8_suffisante"],
            "true":[]
        }'''
    )
    V_5_avec_eau = models.BooleanField(default=False, verbose_name="Y'a-t-il de l'eau(Barafise amazi)?")
    V_6_nb_menages = models.PositiveIntegerField(null=True, verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    V_7_nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    V_8_suffisante = models.BooleanField(default=False, verbose_name="L'eau est-elle suffisante(amazi arakwiye)?")
    V_9_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

class Captage(models.Model):
    class SYSTEME(models.TextChoices):
        GRAVITAIRE = "Système gravitaire"
        POMPAGE = "Pompage"

    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    VI_1_umugende = models.CharField(max_length=64, verbose_name="Nom réseau AEP (Izina ry'umugende ayo mazi yamukako)")
    VI_2_nomination = models.CharField(max_length=128, verbose_name="Nom du captage")
    VI_3_systeme = models.CharField(max_length=32, choices=SYSTEME.choices, verbose_name="Système de captage")
    VI_4_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["VI_5_tarissement","VI_6_protection","VI_7_debit"],
            "true":[]
        }'''
    )
    VI_5_tarissement = models.BooleanField(null=True, verbose_name="Tarissement(Iryo riba rirakama)?")
    VI_6_protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    VI_7_debit = models.FloatField(null=True, verbose_name="Debit de l'eau du système(nombre de littres par seconde)/amalitiro y'amazi yisuka ku musegonda")
    VI_8_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

class Pompe(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    VII_1_nomination = models.CharField(max_length=128, verbose_name="Nom du réseau (Izina ry'umugende)")
    VII_2_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["VII_3_debit"],
            "true":[]
        }'''
    )
    VII_3_debit = models.FloatField(null=True, verbose_name="Debit de l'eau du système(nombre de littres par seconde)/amalitiro y'amazi yisuka ku musegonda")
    VII_4_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

class Puit(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    VII_1_nomination = models.CharField(max_length=128, verbose_name="Nom de la sous colline (Izina ry'agacimbiri kimbweko iryo riba)")
    VII_2_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Harakoreshwa",
        help_text='''{
            "false":["VII_3_coloration","VII_4_nb_menages","VII_5_nb_menages_500","VII_6_tarissement","VII_7_protection"],
            "true":[]
        }'''
    )
    VII_3_coloration = models.BooleanField(null=True, verbose_name="Cette eau est-elle colorée (amazi arafise ibara)?")
    VII_4_nb_menages = models.PositiveIntegerField(null=True, verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    VII_5_nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    VII_6_tarissement = models.BooleanField(null=True, verbose_name="Tarissement(Iryo riba rirakama)?")
    VII_7_protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    VII_8_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

class Forage(models.Model):
    class TYPE(models.TextChoices):
        MANUEL = "Manuel"
        ELECTRIQUE = "Éléctrique"
        SOLAIRE = "Solaire"

    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    XIV_1_type = models.CharField(max_length=32, choices=TYPE.choices)
    XIV_2_nomination = models.CharField(max_length=128, verbose_name="Nom de la sous colline (Izina ry'agacimbiri kimbweko iryo riba)")
    XIV_3_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Harakoreshwa",
        help_text='''{
            "false":["XIV_4_coloration","XIV_5_nb_menages","XIV_6_nb_menages_500","XIV_7_tarissement","XIV_8_protection"],
            "true":[]
        }'''
    )
    XIV_4_coloration = models.BooleanField(default=False)
    XIV_5_nb_menages = models.PositiveIntegerField(null=True, verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    XIV_6_nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    XIV_7_tarissement = models.BooleanField(null=True, verbose_name="Tarissement(Iryo riba rirakama)?")
    XIV_8_protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    XIV_9_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

class Reservoir(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    IX_1_nomination = models.CharField(max_length=128, verbose_name="nom du réseau")
    IX_2_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Irakora",
        help_text='''{
            "false":["IX_3_volume"],
            "true":[]
        }'''
    )
    IX_3_volume = models.FloatField(null=True, verbose_name="le volume du réservoir en mettres cube (ubwaguke bw'ikigega)")
    IX_4_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")

class SourceAmenagee(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    X_1_nomination = models.CharField(max_length=128, verbose_name="Nom de la SA(Izina ry'iryo soko)")
    X_2_sous_colline = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la SA(sous-colline)/ Agacimbiri karimwo iryo soko")
    X_3_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["X_4_coloration","X_8_nb_menages","X_9_nb_menages_500","X_5_tarissement","X_7_protection","X_6_debit"],
            "true":[]
        }'''
    )
    X_4_coloration = models.BooleanField(null=True, verbose_name="Cette eau est-elle colorée (amazi arafise ibara)?")
    X_5_tarissement = models.BooleanField(null=True, verbose_name="Tarissement(Iryo riba rirakama)?")
    X_6_debit = models.FloatField(null=True, verbose_name="Debit de l'eau du système(nombre de littres par seconde)/amalitiro y'amazi yisuka ku musegonda")
    X_7_protection = models.BooleanField(default=False, verbose_name="Existence d'une zone de protection(Hoba hariho uruzitiro rukingira iryo riba?)")
    X_8_nb_menages = models.PositiveIntegerField(null=True, verbose_name="nombre de menages utilisant cette source se trouvant à moins de 500m")
    X_9_nb_menages_500 = models.PositiveIntegerField(default=0, verbose_name="nombre de menages utilisant cette source se trouvant à plus de 500m")
    X_10_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "Sources aménagées"

class SourceNonAmenagee(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    XI_1_nomination = models.CharField(max_length=128, verbose_name="Nom de la SNA(Izina ry'iryo soko)")
    XI_2_fonctionnel = models.BooleanField(
        default=False, verbose_name="Fonctionnel / Rirakora",
        help_text='''{
            "false":["X_3_coloration","X_4_tarissement","X_5_debit","X_6_sous_colline"],
            "true":[]
        }'''
    )
    XI_3_coloration = models.BooleanField(null=True, verbose_name="Cette eau est-elle colorée (amazi arafise ibara)?")
    XI_4_tarissement = models.BooleanField(null=True, verbose_name="Tarissement(Iryo riba rirakama)?")
    XI_5_debit = models.FloatField(null=True, verbose_name="Debit de l'eau du système(nombre de littres par seconde)/amalitiro y'amazi yisuka ku musegonda")
    XI_6_sous_colline = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la SA(sous-colline)/ Agacimbiri karimwo iryo soko")
    XI_7_observations = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "Sources non-aménagées"

class VillageModerne(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    XII_1_nomination = models.CharField(max_length=128, verbose_name="Nom du village (Izina ry'ikigwati)")
    XII_2_fonctionnel = models.BooleanField(
        default=False, verbose_name="Le village est-il alimenté en eau potable/Ico kigwati kirafise amazi?",
        help_text='''{
            "false":["XII_3_province","XII_4_commune","XII_5_source"],
            "true":["XII_6_province_a_capter","XII_7_commune_a_capter","XII_9_source_a_capter"]
        }'''
    )
    XII_3_province = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara irimwo isoko ritanga amazi kuri ico kigwati")
    XII_4_commune = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine irimwo isoko ritanga amazi kuri ico kigwati")
    XII_5_source = models.CharField(null=True, max_length=32, verbose_name="Nom de la source d'eau")
    XII_6_province_a_capter = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara ihegereye wokurako amazi")
    XII_7_commune_a_capter = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine ihegereye wokurako amazi")
    XII_9_source_a_capter = models.CharField(null=True, max_length=32, verbose_name="Nom de la source d'eau à capter(isoko rihegereye wokurako amazi)")
    XII_10_observations = models.CharField(null=True, max_length=128, blank=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "villages modernes"

class VillageCollinaire(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.localdate, editable=False)
    I_1_nom_et_prenom = models.CharField(max_length=64, verbose_name="Nom et prénom")
    I_2_sexe = models.CharField(max_length=8, choices=SEXE.choices, verbose_name="sexe")
    I_3_telephone = models.CharField(max_length=32, verbose_name="telephone")
    II_1_province = models.CharField(max_length=32, verbose_name="province")
    II_2_commune = models.CharField(max_length=32, verbose_name="commune")
    II_3_zone = models.CharField(max_length=32, verbose_name="zone")
    II_4_colline = models.CharField(max_length=32, verbose_name="colline")
    II_5_coordonnees = models.CharField(max_length=64, verbose_name="latitude")
    II_6_milieu = models.CharField(max_length=32, default=MILIEU.RURAL, choices=MILIEU.choices, verbose_name="Milieu")
    XIII_1_nomination = models.CharField(max_length=128, verbose_name="Nom du village (Izina ry'ikigwati)")
    XIII_2_fonctionnel = models.BooleanField(
        default=False, verbose_name="Le village est-il alimenté en eau potable/Ico kigwati kirafise amazi?",
        help_text='''{
            "false":["XIII_3_province","XIII_4_commune","XIII_5_source"],
            "true":["XIII_6_province_a_capter","XIII_7_commune_a_capter","XIII_8_source_a_capter"]
        }'''
    )
    XIII_3_province = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara irimwo isoko ritanga amazi kuri ico kigwati")
    XIII_4_commune = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine irimwo isoko ritanga amazi kuri ico kigwati")
    XIII_5_source = models.CharField(null=True, max_length=32, verbose_name="Nom de la source d'eau")
    XIII_6_province_a_capter = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Province)/Intara ihegereye wokurako amazi")
    XIII_7_commune_a_capter = models.CharField(null=True, max_length=32, verbose_name="Emplacement de la source d'eau(Commune)/Ikomine ihegereye wokurako amazi")
    XIII_8_source_a_capter = models.CharField(null=True, max_length=32, verbose_name="Nom de la source d'eau à capter(isoko rihegereye wokurako amazi)")
    XIII_9_observations = models.CharField(null=True, max_length=128, blank=True, verbose_name="Observations (ivyihwejwe)")
    
    class Meta:
        verbose_name_plural = "Villages collinaires"
