from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()

# router.register("colis", views.ColisViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', views.TokenPairView.as_view()),
    # path('refresh/', TokenRefreshView.as_view())
]
