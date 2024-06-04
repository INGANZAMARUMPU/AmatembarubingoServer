from rest_framework import serializers
from.models import *

class ReseauDAlimentationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseauDAlimentation
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "XV_1_nomination", "XV_2_type", "XV_4_observations"

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data 

class IbomboReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ibombo
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "IV_1_place", "IV_2_identification", "IV_3_umugende", "IV_4_fonctionnel", "IV_5_nb_menages", "IV_6_nb_menages_500", "IV_7_observations"

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data 

class BranchementPriveReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchementPrive
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "V_1_place", "V_2_nomination", "V_3_umugende", "V_4_fonctionnel", "V_5_avec_eau", "V_6_nb_menages", "V_7_nb_menages_500", "V_8_suffisante", "V_9_observations"

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data

class CaptageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captage
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "VI_1_umugende", "VI_2_nomination", "VI_3_systeme", "VI_4_fonctionnel", "VI_5_tarissement", "VI_6_protection", "VI_7_debit", "VI_8_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data

class PompeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pompe
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "VII_1_nomination", "VII_2_fonctionnel", "VII_3_debit", "VII_4_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data

class PuitReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puit
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "VII_1_nomination", "VII_2_fonctionnel", "VII_3_coloration", "VII_4_nb_menages", "VII_5_nb_menages_500", "VII_6_tarissement", "VII_7_protection", "VII_8_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data

class ForageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forage
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "XIV_1_type", "XIV_2_nomination", "XIV_3_fonctionnel", "XIV_4_coloration", "XIV_5_nb_menages", "XIV_6_nb_menages_500", "XIV_7_tarissement", "XIV_8_protection", "XIV_9_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data

class ReservoirReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservoir
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "IX_1_nomination", "IX_2_fonctionnel", "IX_3_volume", "IX_4_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data

class SourceAmenageeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceAmenagee
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "X_1_nomination", "X_2_sous_colline", "X_3_fonctionnel", "X_4_coloration", "X_5_tarissement", "X_6_debit", "X_7_protection", "X_8_nb_menages", "X_9_nb_menages_500", "X_10_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data


class SourceNonAmenageeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceNonAmenagee
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "XI_1_nomination", "XI_2_fonctionnel", "XI_3_coloration", "XI_4_tarissement", "XI_5_debit", "XI_6_sous_colline", "XI_7_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data


class VillageModerneReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageModerne
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "XII_1_nomination", "XII_2_fonctionnel", "XII_3_province", "XII_4_commune", "XII_5_source", "XII_6_province_a_capter", "XII_7_commune_a_capter", "XII_9_source_a_capter", "XII_10_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data


class VillageCollinaireReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageCollinaire
        fields = "date", "II_3_zone", "II_4_colline", "II_5_coordonnees", "XIII_1_nomination", "XIII_2_fonctionnel", "XIII_3_province", "XIII_4_commune", "XIII_5_source", "XIII_6_province_a_capter", "XIII_7_commune_a_capter", "XIII_8_source_a_capter", "XIII_9_observations"
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["II_5_coordonnees"] = " ".join(obj.II_5_coordonnees.split()[:2])
        return data

