from import_export import resources
from.models import *


class ProvinceResource(resources.ModelResource):
    class Meta:
        model = Province


class CommuneResource(resources.ModelResource):
    class Meta:
        model = Commune


class CollineResource(resources.ModelResource):
    class Meta:
        model = Colline


class SousCollineResource(resources.ModelResource):
    class Meta:
        model = SousColline


class EnqueteurResource(resources.ModelResource):
    class Meta:
        model = Enqueteur


class ReseauDAlimentationResource(resources.ModelResource):
    class Meta:
        model = ReseauDAlimentation


class IbomboResource(resources.ModelResource):
    class Meta:
        model = Ibombo


class BranchementPriveResource(resources.ModelResource):
    class Meta:
        model = BranchementPrive


class CaptageResource(resources.ModelResource):
    class Meta:
        model = Captage


class PompeResource(resources.ModelResource):
    class Meta:
        model = Pompe


class PuitResource(resources.ModelResource):
    class Meta:
        model = Puit


class ForageResource(resources.ModelResource):
    class Meta:
        model = Forage


class ReservoirResource(resources.ModelResource):
    class Meta:
        model = Reservoir


class SourceAmenageeResource(resources.ModelResource):
    class Meta:
        model = SourceAmenagee


class SourceNonAmenageeResource(resources.ModelResource):
    class Meta:
        model = SourceNonAmenagee


class VillageModerneResource(resources.ModelResource):
    class Meta:
        model = VillageModerne


class VillageCollinaireResource(resources.ModelResource):
    class Meta:
        model = VillageCollinaire

