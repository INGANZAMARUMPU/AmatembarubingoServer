from rest_framework import serializers
from.models import *

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = "__all__"

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"

class CollineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colline
        fields = "__all__"

class ReseauDAlimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseauDAlimentation
        fields = "__all__"

class IbomboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ibombo
        fields = "__all__"

class BranchementPriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchementPrive
        fields = "__all__"

class CaptageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captage
        fields = "__all__"

class PompeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pompe
        fields = "__all__"

class PuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puit
        fields = "__all__"

class ForageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forage
        fields = "__all__"

class ReservoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservoir
        fields = "__all__"

class SourceAmenageeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceAmenagee
        fields = "__all__"

class SourceNonAmenageeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceNonAmenagee
        fields = "__all__"

class VillageModerneSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageModerne
        fields = "__all__"

class VillageCollinaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageCollinaire
        fields = "__all__"
