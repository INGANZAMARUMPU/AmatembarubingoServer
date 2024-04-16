from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .ressources import *

@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProvinceResource
    list_display = "nom",

@admin.register(Commune)
class CommuneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommuneResource
    list_display = "nom", "province"

@admin.register(Zone)
class ZoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ZoneResource
    list_display = "nom", "commune"

@admin.register(Colline)
class CollineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CollineResource
    list_display = "nom", "zone"
    search_fields = "nom", "zone__nom", "zone__commune__nom"

@admin.register(Enqueteur)
class EnqueteurAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EnqueteurResource
    list_display = "nom", "prenom", "telephone", "sexe"

@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReseauDAlimentationResource
    list_display =  "colline", "enqueteur", "code", "nom", "date", "type", "observations"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(Ibombo)
class IbomboAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = IbomboResource
    list_display = "colline", "map", "identification", "umugende", "fonctionnel", "nb_menages", "nb_menages_500", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(BranchementPrive)
class BranchementPriveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BranchementPriveResource
    list_display = "colline", "map", "nom", "umugende", "fonctionnel", "nb_menages", "nb_menages_500", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(Captage)
class CaptageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CaptageResource
    list_display = "colline", "map", "altitude", "code", "code_reseau", "nom", "precision", "fonctionnel", "tarissement", "protection", "debit", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(Pompe)
class PompeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PompeResource
    list_display = "colline", "map", "altitude", "code", "code_reseau", "nom", "precision", "fonctionnel", "debit", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(Puit)
class PuitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PuitResource
    list_display = "colline", "map", "nature", "nom", "date_forage", "fonctionnel", "coloration", "nb_menages", "nb_menages_500", "tarissement", "protection", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(Forage)
class ForageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ForageResource
    list_display = "colline", "map", "nature", "nom", "date_forage", "fonctionnel", "coloration", "nb_menages", "nb_menages_500", "tarissement", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(Reservoir)
class ReservoirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReservoirResource
    list_display = "colline", "map", "code_reservoir", "code_reseau", "nom", "fonctionnel", "volume", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(SourceAmenagee)
class SourceAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceAmenageeResource
    list_display = "colline", "map", "nom", "fonctionnel", "coloration", "tarissement", "protection", "nb_menages", "nb_menages_500", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(SourceNonAmenagee)
class SourceNonAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceNonAmenageeResource
    list_display = "colline", "map", "code", "nom", "coloration", "tarissement", "debit", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(VillageModerne)
class VillageModerneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageModerneResource
    list_display = "colline", "map", "code", "nom", "alimentation_potable", "source_a_capter", "debit", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")

@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageCollinaireResource
    list_display = "colline", "map", "code", "nom", "alimentation_potable", "source_a_capter", "debit", "enqueteur"

    def map(self, obj):
        return mark_safe(f"<a target=blank href='https://maps.google.com/?q={obj.latitude},{obj.longitude}&ll={obj.latitude},{obj.longitude}&z=18'>voir sur la carte</a>")