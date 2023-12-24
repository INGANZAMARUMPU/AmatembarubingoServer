from django.contrib import admin
from.models import *

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    display_fields = "nom"


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    display_fields = "nom", "province"


@admin.register(Colline)
class CollineAdmin(admin.ModelAdmin):
    display_fields = "nom", "commune"


@admin.register(SousColline)
class SousCollineAdmin(admin.ModelAdmin):
    display_fields = "nom", "colline", "latitude", "longitude"


@admin.register(Enqueteur)
class EnqueteurAdmin(admin.ModelAdmin):
    display_fields = "user", "telephone", "colline"


@admin.register(Localisation)
class LocalisationAdmin(admin.ModelAdmin):
    display_fields = "latitude", "longitude", "altitude", "precision"


@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(admin.ModelAdmin):
    display_fields = "code", "nom", "date", "enqueteur", "localisation", "sous_colline", "gravitaire", "pompage", "lineaire_km", "gestionnaire", "nb_captages", "nb_pompes", "nb_reservoirs", "nb_bornes_fontaines_publiques", "nb_branchements_prives", "nb_menages", "observations"


@admin.register(Ibombo)
class IbomboAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "localisation", "date", "nom", "umugende", "fonctionnel", "nb_menages", "observations"


@admin.register(BranchementPrive)
class BranchementPriveAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "localisation", "nom", "umugende", "date", "sous_colline", "fonctionnel", "nb_menages", "observations"


@admin.register(Pompe)
class PompeAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "code", "code_reseau", "nom", "date", "sous_colline", "localisation", "fonctionnel", "observations"


@admin.register(Puit)
class PuitAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "nature", "nom", "date_forage", "date", "sous_colline", "localisation", "fonctionnel", "coloration", "nb_menages", "tarissement", "cloture", "observations"


@admin.register(Reservoir)
class ReservoirAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "code_reservoir", "code_reseau", "nom", "date", "sous_colline", "localisation", "fonctionnel", "volume_en_m3", "observations"


@admin.register(RusengoYubakiye)
class RusengoYubakiyeAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "nom", "date", "sous_colline", "localisation", "fonctionnel", "coloration", "tarissement", "cloture", "nb_menages", "observations"


@admin.register(SourceNonAmenage)
class SourceNonAmenageAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "localisation", "coloration", "odeur", "tarissement", "debit", "observations"


@admin.register(VillageModerne)
class VillageModerneAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "alimentation_potable", "source_a_capter", "debit", "localisation", "observations"


@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(admin.ModelAdmin):
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "alimentation_potable", "source_a_capter", "debit", "localisation", "observations"


