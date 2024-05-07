import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AmatembarubingoServer.settings")

import django
django.setup()

from api.models import *
import tqdm

tables = [
    ReseauDAlimentation, Ibombo, BranchementPrive, Captage, Pompe, Puit, Forage, Reservoir, SourceAmenagee, SourceNonAmenagee, VillageModerne, VillageCollinaire
]
for table in tables:
    for item in tqdm(table.objects.values('II_5_coordonnees').distinct()):
        wrongs = table.objects.filter(II_5_coordonnees=item.II_5_coordonnees).exclude(id=item.id).delete()
