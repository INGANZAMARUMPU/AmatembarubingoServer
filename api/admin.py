from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .ressources import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = "nom", "fichier", "details"

@admin.register(Manuel)
class ManuelAdmin(admin.ModelAdmin):
    list_display = "nom", "fichier", "details"

@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProvinceResource

@admin.register(Commune)
class CommuneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommuneResource

@admin.register(Zone)
class ZoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ZoneResource
    list_display = "nom", "commune"
    list_filter = "commune",

@admin.register(Colline)
class CollineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CollineResource
    list_display = "nom", "zone"
    list_filter = "zone",

@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReseauDAlimentationResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "XV_1_nomination", "XV_2_type", "XV_4_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline",
    

@admin.register(Ibombo)
class IbomboAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = IbomboResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "IV_1_place", "IV_2_identification", "IV_3_umugende", "IV_4_fonctionnel", "IV_5_nb_menages", "IV_6_nb_menages_500", "IV_7_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "IV_4_fonctionnel", "IV_5_nb_menages", "IV_6_nb_menages_500",
    

@admin.register(BranchementPrive)
class BranchementPriveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BranchementPriveResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "V_1_place", "V_2_nomination", "V_3_umugende", "V_4_fonctionnel", "V_5_avec_eau", "V_6_nb_menages", "V_7_nb_menages_500", "V_8_suffisante", "V_9_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "V_4_fonctionnel", "V_6_nb_menages", "V_7_nb_menages_500",

@admin.register(Captage)
class CaptageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CaptageResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "VI_1_umugende", "VI_2_nomination", "VI_3_systeme", "VI_4_fonctionnel", "VI_5_tarissement", "VI_6_protection", "VI_7_debit", "VI_8_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "VI_4_fonctionnel"

@admin.register(Pompe)
class PompeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PompeResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "VII_1_nomination", "VII_2_fonctionnel", "VII_3_debit", "VII_4_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "VII_2_fonctionnel"

@admin.register(Puit)
class PuitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PuitResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "VII_1_nomination", "VII_2_fonctionnel", "VII_3_coloration", "VII_4_nb_menages", "VII_5_nb_menages_500", "VII_6_tarissement", "VII_7_protection", "VII_8_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "VII_2_fonctionnel", "VII_4_nb_menages", "VII_5_nb_menages_500",

@admin.register(Forage)
class ForageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ForageResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "XIV_1_type", "XIV_2_nomination", "XIV_3_fonctionnel", "XIV_4_coloration", "XIV_5_nb_menages", "XIV_6_nb_menages_500", "XIV_7_tarissement", "XIV_8_protection", "XIV_9_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "XIV_3_fonctionnel", "XIV_5_nb_menages", "XIV_6_nb_menages_500",

@admin.register(Reservoir)
class ReservoirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ReservoirResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "IX_1_nomination", "IX_2_fonctionnel", "IX_3_volume", "IX_4_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "IX_2_fonctionnel"

@admin.register(SourceAmenagee)
class SourceAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceAmenageeResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "X_1_nomination", "X_2_sous_colline", "X_3_fonctionnel", "X_4_coloration", "X_5_tarissement", "X_6_debit", "X_7_protection", "X_8_nb_menages", "X_9_nb_menages_500", "X_10_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "X_3_fonctionnel", "X_8_nb_menages", "X_9_nb_menages_500",


@admin.register(SourceNonAmenagee)
class SourceNonAmenageeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SourceNonAmenageeResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "XI_1_nomination", "XI_2_fonctionnel", "XI_3_coloration", "XI_4_tarissement", "XI_5_debit", "XI_6_sous_colline", "XI_7_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "XI_2_fonctionnel"


@admin.register(VillageModerne)
class VillageModerneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageModerneResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "XII_1_nomination", "XII_2_fonctionnel", "XII_3_province", "XII_4_commune", "XII_5_source", "XII_6_province_a_capter", "XII_7_commune_a_capter", "XII_9_source_a_capter", "XII_10_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "XII_2_fonctionnel"


@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VillageCollinaireResource
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_coordonnees", "II_6_milieu", "XIII_1_nomination", "XIII_2_fonctionnel", "XIII_3_province", "XIII_4_commune", "XIII_5_source", "XIII_6_province_a_capter", "XIII_7_commune_a_capter", "XIII_8_source_a_capter", "XIII_9_observations"
    list_filter = "date", "I_1_nom_et_prenom", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "XIII_2_fonctionnel"


@admin.register(CarteThematique)
class CarteThematiqueAdmin(admin.ModelAdmin):
    list_display = "theme", "carte", "details"
