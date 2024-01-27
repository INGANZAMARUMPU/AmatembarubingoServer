from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .ressources import *

@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProvinceResource
    display_fields = "nom",

@admin.register(Commune)
class CommuneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommuneResource
    display_fields = "nom", "province"

@admin.register(Zone)
class ZoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ZoneResource
    display_fields = "nom", "commune"

@admin.register(Colline)
class CollineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CollineResource
    display_fields = "nom", "zone"
    search_fields = "nom", "zone__nom", "zone__commune__nom"

@admin.register(Enqueteur)
class EnqueteurAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EnqueteurResource
    display_fields = "user", "telephone", "colline"

@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReseauDAlimentationResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "code", "nom", "date", "gravitaire", "pompage", "lineaire_km", "gestionnaire", "nb_captages", "nb_pompes", "nb_reservoirs", "nb_bornes_fontaines_publiques", "nb_branchements_prives", "nb_menages", "observations"

@admin.register(Ibombo)
class IbomboAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = IbomboResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "date", "nom", "umugende", "fonctionnel", "nb_menages", "observations"

@admin.register(BranchementPrive)
class BranchementPriveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BranchementPriveResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "nom", "umugende", "date", "fonctionnel", "nb_menages", "observations"

@admin.register(Captage)
class CaptageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CaptageResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "code", "code_reseau", "nom", "date", "precision", "fonctionnel", "tarissement", "protection", "debit", "observations"

@admin.register(Pompe)
class PompeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PompeResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "code", "code_reseau", "nom", "date", "precision", "fonctionnel", "debit", "observations"

@admin.register(Puit)
class PuitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PuitResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "nature", "nom", "date_forage", "date", "fonctionnel", "coloration", "nb_menages", "tarissement", "protection", "observations"

@admin.register(Forage)
class ForageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ForageResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "nature", "nom", "date_forage", "date", "fonctionnel", "coloration", "nb_menages", "tarissement", "observations"

@admin.register(Reservoir)
class ReservoirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReservoirResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "code_reservoir", "code_reseau", "nom", "date", "fonctionnel", "volume", "observations"

@admin.register(SourceAmenagee)
class SourceAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceAmenageeResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "nom", "date", "fonctionnel", "coloration", "tarissement", "protection", "nb_menages", "observations"

@admin.register(SourceNonAmenagee)
class SourceNonAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceNonAmenageeResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "code", "nom", "date", "coloration", "tarissement", "debit", "observations"

@admin.register(VillageModerne)
class VillageModerneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageModerneResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "code", "nom", "date", "alimentation_potable", "source_a_capter", "debit", "observations"

@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageCollinaireResource
    display_fields = "enqueteur", "colline", "latitude", "longitude", "altitude", "precision", "code", "nom", "date", "alimentation_potable", "source_a_capter", "debit", "observations"