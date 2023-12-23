from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import settings

admin.site.site_header = 'AMAZI MEZA HOSE'
admin.site.index_title = 'haruguru'
admin.site.site_title = 'Ubugenduzi'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
	path('api-auth/', include('rest_framework.urls')),
    re_path(
        "^(?!media)(?!admin)(?!api)(?!static).*$",
        TemplateView.as_view(template_name='index.html')
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
