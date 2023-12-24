from django.contrib import admin
from.models import *

class PermissiveModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        user:User = request.user
        groups = {x.name.lower() for x in user.groups.all()}
        return "admin" in groups or "enqueteur" in groups or user.is_superuser

    def has_change_permission(self, request, obj=None):
        user:User = request.user
        groups = {x.name.lower() for x in user.groups.all()}
        return "admin" in groups or user.is_superuser

    def has_delete_permission(self, request, obj=None):
        user:User = request.user
        groups = {x.name.lower() for x in user.groups.all()}
        return "admin" in groups or user.is_superuser

@admin.register(Province)
class ProvinceAdmin(PermissiveModelAdmin):
    display_fields = "nom"


@admin.register(Commune)
class CommuneAdmin(PermissiveModelAdmin):
    display_fields = "nom", "province"


@admin.register(Colline)
class CollineAdmin(PermissiveModelAdmin):
    display_fields = "nom", "commune"


@admin.register(SousColline)
class SousCollineAdmin(PermissiveModelAdmin):
    display_fields = "nom", "colline", "latitude", "longitude"


@admin.register(Enqueteur)
class EnqueteurAdmin(PermissiveModelAdmin):
    display_fields = "user", "telephone", "colline"


@admin.register(Localisation)
class LocalisationAdmin(PermissiveModelAdmin):
    display_fields = "latitude", "longitude", "altitude", "precision"


@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(PermissiveModelAdmin):
    display_fields = "code", "nom", "date", "enqueteur", "localisation", "sous_colline", "gravitaire", "pompage", "lineaire_km", "gestionnaire", "nb_captages", "nb_pompes", "nb_reservoirs", "nb_bornes_fontaines_publiques", "nb_branchements_prives", "nb_menages", "observations"


@admin.register(Ibombo)
class IbomboAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "localisation", "date", "nom", "umugende", "fonctionnel", "nb_menages", "observations"


@admin.register(BranchementPrive)
class BranchementPriveAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "localisation", "nom", "umugende", "date", "sous_colline", "fonctionnel", "nb_menages", "observations"


@admin.register(Pompe)
class PompeAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "code", "code_reseau", "nom", "date", "sous_colline", "localisation", "fonctionnel", "observations"


@admin.register(Puit)
class PuitAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "nature", "nom", "date_forage", "date", "sous_colline", "localisation", "fonctionnel", "coloration", "nb_menages", "tarissement", "cloture", "observations"


@admin.register(Reservoir)
class ReservoirAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "code_reservoir", "code_reseau", "nom", "date", "sous_colline", "localisation", "fonctionnel", "volume_en_m3", "observations"


@admin.register(RusengoYubakiye)
class RusengoYubakiyeAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "nom", "date", "sous_colline", "localisation", "fonctionnel", "coloration", "tarissement", "cloture", "nb_menages", "observations"


@admin.register(SourceNonAmenagee)
class SourceNonAmenageeAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "localisation", "coloration", "odeur", "tarissement", "debit", "observations"


@admin.register(VillageModerne)
class VillageModerneAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "alimentation_potable", "source_a_capter", "debit", "localisation", "observations"


@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(PermissiveModelAdmin):
    display_fields = "enqueteur", "code", "nom", "date", "sous_colline", "alimentation_potable", "source_a_capter", "debit", "localisation", "observations"


