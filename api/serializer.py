from rest_framework import serializer
from.models import *


class ProvinceSerializer(serializer.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"

class CommuneSerializer(serializer.ModelSerializer):
    class Meta:
        model = Commune
        fields = "__all__"

class ZoneSerializer(serializer.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"

class CollineSerializer(serializer.ModelSerializer):
    class Meta:
        model = Colline
        fields = "__all__"

class EnqueteurSerializer(serializer.ModelSerializer):
    class Meta:
        model = Enqueteur
        fields = "__all__"

class ReseauDAlimentationSerializer(serializer.ModelSerializer):
    class Meta:
        model = ReseauDAlimentation
        fields = "__all__"

class IbomboSerializer(serializer.ModelSerializer):
    class Meta:
        model = Ibombo
        fields = "__all__"

class BranchementPriveSerializer(serializer.ModelSerializer):
    class Meta:
        model = BranchementPrive
        fields = "__all__"

class CaptageSerializer(serializer.ModelSerializer):
    class Meta:
        model = Captage
        fields = "__all__"

class PompeSerializer(serializer.ModelSerializer):
    class Meta:
        model = Pompe
        fields = "__all__"

class PuitSerializer(serializer.ModelSerializer):
    class Meta:
        model = Puit
        fields = "__all__"

class ForageSerializer(serializer.ModelSerializer):
    class Meta:
        model = Forage
        fields = "__all__"

class ReservoirSerializer(serializer.ModelSerializer):
    class Meta:
        model = Reservoir
        fields = "__all__"

class SourceAmenageeSerializer(serializer.ModelSerializer):
    class Meta:
        model = SourceAmenagee
        fields = "__all__"

class SourceNonAmenageeSerializer(serializer.ModelSerializer):
    class Meta:
        model = SourceNonAmenagee
        fields = "__all__"

class VillageModerneSerializer(serializer.ModelSerializer):
    class Meta:
        model = VillageModerne
        fields = "__all__"

class VillageCollinaireSerializer(serializer.ModelSerializer):
    class Meta:
        model = VillageCollinaire
        fields = "__all__"
