from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from .models import *
from .serializers import *

class CollineViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Colline.objects.all()
    serializer_class = CollineSerializer

class ReseauDAlimentationViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = ReseauDAlimentation.objects.all()
    serializer_class = ReseauDAlimentationSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class IbomboViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Ibombo.objects.all()
    serializer_class = IbomboSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class BranchementPriveViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = BranchementPrive.objects.all()
    serializer_class = BranchementPriveSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class CaptageViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Captage.objects.all()
    serializer_class = CaptageSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class PompeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Pompe.objects.all()
    serializer_class = PompeSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class PuitViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Puit.objects.all()
    serializer_class = PuitSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class ForageViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Forage.objects.all()
    serializer_class = ForageSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class ReservoirViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = Reservoir.objects.all()
    serializer_class = ReservoirSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class SourceAmenageeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = SourceAmenagee.objects.all()
    serializer_class = SourceAmenageeSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class SourceNonAmenageeViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = SourceNonAmenagee.objects.all()
    serializer_class = SourceNonAmenageeSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class VillageModerneViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = VillageModerne.objects.all()
    serializer_class = VillageModerneSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }

class VillageCollinaireViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = AllowAny,
    queryset = VillageCollinaire.objects.all()
    serializer_class = VillageCollinaireSerializer
    filter_backends = filters.DjangoFilterBackend,
    filterset_fields = {
        'colline': ['exact']
    }
