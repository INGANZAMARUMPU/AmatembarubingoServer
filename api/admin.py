from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .ressources import *

@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProvinceResource
    display_fields = "nom"


@admin.register(Commune)
class CommuneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommuneResource
    display_fields = "nom", "province"


@admin.register(Colline)
class CollineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CollineResource
    display_fields = "nom", "commune"


@admin.register(SousColline)
class SousCollineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SousCollineResource
    display_fields = "nom", "colline", "latitude", "longitude"


@admin.register(Enqueteur)
class EnqueteurAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EnqueteurResource
    display_fields = "user", "telephone", "colline"

@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReseauDAlimentationResource
    display_fields = "code", "nom", "date", "enqueteur", "latitude", "longitude", "altitude", "sous_colline", "gravitaire", "pompage", "lineaire_km", "gestionnaire", "nb_captages", "nb_pompes", "nb_reservoirs", "nb_bornes_fontaines_publiques", "nb_branchements_prives", "nb_menages", "observations"


@admin.register(Ibombo)
class IbomboAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = IbomboResource
    display_fields = "enqueteur", "latitude", "longitude", "altitude", "date", "nom", "umugende", "fonctionnel", "nb_menages", "observations"


@admin.register(BranchementPrive)
class BranchementPriveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BranchementPriveResource
    display_fields = "enqueteur", "latitude", "longitude", "altitude", "nom", "umugende", "date", "sous_colline", "fonctionnel", "nb_menages", "observations"


@admin.register(Pompe)
class PompeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PompeResource
    display_fields = "enqueteur", "code", "code_reseau", "nom", "date", "sous_colline", "latitude", "longitude", "altitude", "fonctionnel", "observations"


@admin.register(Puit)
class PuitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PuitResource
    display_fields = "enqueteur", "nature", "nom", "date_forage", "date", "sous_colline", "latitude", "longitude", "altitude", "fonctionnel", "coloration", "nb_menages", "tarissement", "cloture", "observations"


@admin.register(Reservoir)
class ReservoirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReservoirResource
    display_fields = "enqueteur", "code_reservoir", "code_reseau", "nom", "date", "sous_colline", "latitude", "longitude", "altitude", "fonctionnel", "volume_en_m3", "observations"


@admin.register(RusengoYubakiye)
class RusengoYubakiyeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RusengoYubakiyeResource
    display_fields = "enqueteur", "nom", "date", "sous_colline", "latitude", "longitude", "altitude", "fonctionnel", "coloration", "tarissement", "cloture", "nb_menages", "observations"


@admin.register(SourceNonAmenagee)
class SourceNonAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceNonAmenageeResource
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "latitude", "longitude", "altitude", "coloration", "odeur", "tarissement", "debit", "observations"


@admin.register(VillageModerne)
class VillageModerneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageModerneResource
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "alimentation_potable", "source_a_capter", "debit", "latitude", "longitude", "altitude", "observations"


@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageCollinaireResource
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "alimentation_potable", "source_a_capter", "debit", "latitude", "longitude", "altitude", "observations"


