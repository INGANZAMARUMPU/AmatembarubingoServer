import json
import os
from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from tqdm import tqdm

from .models import *
from .serializers import *

def getCentre(queryset:models.QuerySet) -> tuple:
    by_latitudes = queryset.order_by("-latitude")
    by_longitudes = queryset.order_by("-longitude")
    
    max_long = by_longitudes.first().longitude
    min_long = by_longitudes.last().longitude

    max_lat = by_latitudes.first().latitude
    min_lat = by_latitudes.last().latitude

    return max_lat+min_lat/2, max_long+min_long/2

def groupedTemplate(queryset:models.QuerySet, serializer):
    provinces = Province.objects.all()
    response = {
        "count": queryset.count()
    }
    response["data"] = ProvinceSerializer(provinces, many=True).data
    filename = queryset.model.__name__
    
    print(f"[GUPAKURURA] {filename}")
    for province in tqdm(response["data"]):
        province_query = queryset.filter(colline__zone__commune__province_id=province["id"])
        province["count"] = province_query.count()
        province["data"] = CommuneSerializer(Commune.objects.filter(province_id=province["id"]), many=True).data
        for commune in province["data"]:
            commune_query = queryset.filter(colline__zone__commune_id=commune["id"])
            commune["count"] = commune_query.count()
            commune["data"] = ZoneSerializer(Zone.objects.filter(commune_id=commune["id"]), many=True).data
            for zone in commune["data"]:
                zone_query = queryset.filter(colline__zone_id=zone["id"])
                zone["count"] = zone_query.count()
                zone["data"] = CollineSerializer(Colline.objects.filter(zone_id=zone["id"]), many=True).data
                for colline in zone["data"]:
                    colline_query = queryset.filter(colline_id=colline["id"])
                    colline["count"] = colline_query.count()
                    colline["data"] = serializer(colline_query.filter(colline_id=colline["id"]), many=True).data

    with open(filename, "w") as file:
        print(json.dumps(response), file=file)

class CollineViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Colline.objects.all()
    serializer_class = CollineSerializer

    @action( methods=["GET"], detail=False, url_name=r"generate_summaries", url_path=r"generate_summaries" )
    def generate_summaries(self, request):
        groupedTemplate(ReseauDAlimentation.objects.all(), ReseauDAlimentationSerializer)
        groupedTemplate(Ibombo.objects.all(), IbomboSerializer)
        groupedTemplate(BranchementPrive.objects.all(), BranchementPriveSerializer)
        groupedTemplate(Captage.objects.all(), CaptageSerializer)
        groupedTemplate(Pompe.objects.all(), PompeSerializer)
        groupedTemplate(Puit.objects.all(), PuitSerializer)
        groupedTemplate(Forage.objects.all(), ForageSerializer)
        groupedTemplate(Reservoir.objects.all(), ReservoirSerializer)
        groupedTemplate(SourceAmenagee.objects.all(), SourceAmenageeSerializer)
        groupedTemplate(SourceNonAmenagee.objects.all(), SourceNonAmenageeSerializer)
        groupedTemplate(VillageModerne.objects.all(), VillageModerneSerializer)
        groupedTemplate(VillageCollinaire.objects.all(), VillageCollinaireSerializer)
        return Response({"status": "Vyose vyashizwe ku gihe"}, 200)

class ReseauDAlimentationViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = ReseauDAlimentation.objects.all()
    serializer_class = ReseauDAlimentationSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)

class IbomboViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Ibombo.objects.all()
    serializer_class = IbomboSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class BranchementPriveViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = BranchementPrive.objects.all()
    serializer_class = BranchementPriveSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class CaptageViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Captage.objects.all()
    serializer_class = CaptageSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class PompeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Pompe.objects.all()
    serializer_class = PompeSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class PuitViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Puit.objects.all()
    serializer_class = PuitSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class ForageViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Forage.objects.all()
    serializer_class = ForageSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class ReservoirViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Reservoir.objects.all()
    serializer_class = ReservoirSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class SourceAmenageeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = SourceAmenagee.objects.all()
    serializer_class = SourceAmenageeSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class SourceNonAmenageeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = SourceNonAmenagee.objects.all()
    serializer_class = SourceNonAmenageeSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class VillageModerneViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = VillageModerne.objects.all()
    serializer_class = VillageModerneSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)


class VillageCollinaireViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = VillageCollinaire.objects.all()
    serializer_class = VillageCollinaireSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact'],
        'colline__zone': ['exact'],
        'colline__zone__commune': ['exact']
    }

    @action( methods=["GET"], detail=False, url_name=r"grouped", url_path=r"grouped" )
    def grouped(self, request):
        filename = self.get_queryset().model.__name__
        response = None
        try:
            with open(filename, "r") as file:
                content = file.read()
                response = json.loads(content)
                return Response(response, 200)
        except Exception as e:
                return Response({"status": str(e)}, 400)

