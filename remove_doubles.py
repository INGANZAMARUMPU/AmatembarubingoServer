import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AmatembarubingoServer.settings")

import django
import csv
django.setup()

from api.models import *
from django.forms.models import model_to_dict
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
        for coords in tqdm(table.objects.values('II_5_coordonnees').distinct()):
            object = table.objects.filter(II_5_coordonnees = coords).first()
            item = model_to_dict(object)
            # wrongs = table.objects.filter(II_5_coordonnees=item["II_5_coordonnees"]).exclude(id=item.id).delete()
            for key, value in item.items():
                if key not in titles:
                    titles.append(key)
            content = list(titles)
            for i, key in enumerate(content):
                content[i] = item.get(key) or ""
            contents.append(content)
        break

print(contents)
                
            

