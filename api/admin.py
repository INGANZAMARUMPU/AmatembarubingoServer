from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .ressources import *

@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProvinceResource

@admin.register(Commune)
class CommuneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommuneResource

@admin.register(Zone)
class ZoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ZoneResource

@admin.register(Colline)
class CollineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CollineResource

@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReseauDAlimentationResource

@admin.register(Ibombo)
class IbomboAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = IbomboResource

@admin.register(BranchementPrive)
class BranchementPriveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BranchementPriveResource

@admin.register(Captage)
class CaptageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CaptageResource

@admin.register(Pompe)
class PompeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PompeResource

@admin.register(Puit)
class PuitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PuitResource

@admin.register(Forage)
class ForageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ForageResource

@admin.register(Reservoir)
class ReservoirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReservoirResource

@admin.register(SourceAmenagee)
class SourceAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceAmenageeResource

@admin.register(SourceNonAmenagee)
class SourceNonAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceNonAmenageeResource

@admin.register(VillageModerne)
class VillageModerneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageModerneResource

@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageCollinaireResource
