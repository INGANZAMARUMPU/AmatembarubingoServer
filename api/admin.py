from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .ressources import *

@admin.register(ReseauDAlimentation)
class ReseauDAlimentationAdmin(admin.ModelAdmin):
    list_display = "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "XV_1_nomination", "XV_2_type", "XV_3_date", "XV_4_observations"

@admin.register(Ibombo)
class IbomboAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_2_sexe", "I_3_telephone", "II_1_province", "II_2_commune", "II_3_zone", "II_4_colline", "II_5_latitude", "IV_1_place", "IV_2_identification", "IV_3_umugende", "IV_4_fonctionnel", "IV_5_nb_menages", "IV_6_nb_menages_500", "IV_7_observations"


@admin.register(BranchementPrive)
class BranchementPriveAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "V_1_place", "V_2_nomination", "V_3_umugende", "V_4_fonctionnel", "V_5_avec_eau", "V_6_nb_menages", "V_7_nb_menages_500", "V_8_suffisante", "V_9_observations"


@admin.register(Captage)
class CaptageAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "VI_1_umugende", "VI_2_nomination", "VI_3_systeme", "VI_4_fonctionnel", "VI_5_tarissement", "VI_6_protection", "VI_7_debit", "VI_8_observations"

@admin.register(Pompe)
class PompeAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "VII_1_nomination", "VII_2_fonctionnel", "VII_3_debit", "VII_4_observations"

@admin.register(Puit)
class PuitAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "VII_1_nomination", "VII_2_fonctionnel", "VII_3_coloration", "VII_4_nb_menages", "VII_5_nb_menages_500", "VII_6_tarissement", "VII_7_protection", "VII_8_observations"

@admin.register(Forage)
class ForageAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "XIV_1_type", "XIV_2_nomination", "XIV_3_fonctionnel", "XIV_4_coloration", "XIV_5_nb_menages", "XIV_6_nb_menages_500", "XIV_7_tarissement", "XIV_8_protection", "XIV_9_observations"

@admin.register(Reservoir)
class ReservoirAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "IX_1_nomination", "IX_2_fonctionnel", "IX_3_volume", "IX_4_observations"

@admin.register(SourceAmenagee)
class SourceAmenageeAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "X_1_nomination", "X_2_sous_colline", "X_3_fonctionnel", "X_4_coloration", "X_5_tarissement", "X_6_debit", "X_7_protection", "X_8_nb_menages", "X_9_nb_menages_500", "X_10_observations"

@admin.register(SourceNonAmenagee)
class SourceNonAmenageeAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "X_1_nomination", "X_2_fonctionnel", "X_3_coloration", "X_4_tarissement", "X_5_sous_colline", "X_6_observations"

@admin.register(VillageModerne)
class VillageModerneAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "XII_1_nomination", "XII_2_fonctionnel", "XII_3_province", "XII_4_commune", "XII_5_source", "XII_6_province_a_capter", "XII_7_commune_a_capter", "XII_9_source_a_capter", "XII_10_observations"

@admin.register(VillageCollinaire)
class VillageCollinaireAdmin(admin.ModelAdmin):
    list_display = "date", "I_1_nom_et_prenom", "I_1_sexe", "I_1_telephone", "II_1_province", "II_1_commune", "II_1_zone", "II_1_colline", "II_5_latitude", "XIII_1_nomination", "XIII_2_fonctionnel", "XIII_3_province", "XIII_4_commune", "XIII_5_source", "XIII_6_province_a_capter", "XIII_7_commune_a_capter", "XIII_8_source_a_capter", "XIII_9_observations"
