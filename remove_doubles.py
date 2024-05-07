import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AmatembarubingoServer.settings")

import django
import csv
django.setup()

from api.models import *
from tqdm import tqdm

tables:list[models.Model] = [
    ReseauDAlimentation, Ibombo, BranchementPrive, Captage, Pompe, Puit, Forage, Reservoir,
    SourceAmenagee, SourceNonAmenagee, VillageModerne, VillageCollinaire
]
titles = []
contents = []

with open("db.csv", "+a") as file:
    for table in tables:
        table.objects.filter(date__lt=datetime.date(2024, 5, 7)).delete()
        for item in tqdm(table.objects.values('II_5_coordonnees').distinct()):
            # wrongs = table.objects.filter(II_5_coordonnees=item["II_5_coordonnees"]).exclude(id=item.id).delete()
            for key, value in item:
                if key not in titles:
                    titles.append(key)
            content = list(titles)
            for i, key in enumerate(content):
                content[i] = item.get(key) or ""
            contents.append(content)
        break

print(contents)
                
            

