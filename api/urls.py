from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import *

router = routers.DefaultRouter()
router.register("provinces", ProvinceViewset)
router.register("collines", CollineViewset)
router.register("reseaudalimentations", ReseauDAlimentationViewset)
router.register("amabombo", IbomboViewset)
router.register("branchementprives", BranchementPriveViewset)
router.register("captages", CaptageViewset)
router.register("pompes", PompeViewset)
router.register("puits", PuitViewset)
router.register("forages", ForageViewset)
router.register("reservoirs", ReservoirViewset)
router.register("sourceamenagees", SourceAmenageeViewset)
router.register("sourcenonamenagees", SourceNonAmenageeViewset)
router.register("villagemodernes", VillageModerneViewset)
router.register("villagecollinaires", VillageCollinaireViewset)

urlpatterns = [
	path("", include(router.urls)),
    path('refresh/', TokenRefreshView.as_view()),
]
