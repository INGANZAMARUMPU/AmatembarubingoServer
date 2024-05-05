from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .ressources import *

admin.site.register(Province)
admin.site.register(Commune)
admin.site.register(Zone)
admin.site.register(Colline)
admin.site.register(ReseauDAlimentation)
admin.site.register(Ibombo)
admin.site.register(BranchementPrive)
admin.site.register(Captage)
admin.site.register(Pompe)
admin.site.register(Puit)
admin.site.register(Forage)
admin.site.register(Reservoir)
admin.site.register(SourceAmenagee)
admin.site.register(SourceNonAmenagee)
admin.site.register(VillageModerne)
admin.site.register(VillageCollinaire)