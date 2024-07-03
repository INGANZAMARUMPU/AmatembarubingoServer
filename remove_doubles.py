import datetime

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AmatembarubingoServer.settings")
import django
django.setup()

from api.views import *
from django.forms.models import model_to_dict
from tqdm import tqdm

list_viewsets:list[viewsets.ModelViewSet] = [
    IbomboViewset,
    BranchementPriveViewset,
    CaptageViewset,
    PompeViewset,
    PuitViewset,
    ReservoirViewset,
    SourceAmenageeViewset,
    SourceNonAmenageeViewset,
    VillageModerneViewset,
    VillageCollinaireViewset,
    ForageViewset,
    ReseauDAlimentationViewset,
]

titles = ["I. Formulaire", "date"]
contents = []

print("TRAITEMENT")
for viewset_class in list_viewsets:
    viewset = viewset_class()
    table:models.QuerySet = viewset.get_queryset().filter(
#        date__gte = datetime.date(2024, 6, 23),
        date__lt = datetime.date(2024, 7, 1)
    )
    table.delete()
    continue
    for coords in tqdm(table.values('II_5_coordonnees').distinct()):
        object = table.filter(II_5_coordonnees = coords["II_5_coordonnees"]).first()
        item = model_to_dict(object)
        # wrongs = table.objects.filter(II_5_coordonnees=item["II_5_coordonnees"]).exclude(id=item.id).delete()
        new_item = {}
        for key, value in item.items():
            keys = key.split("_")
            if len(keys) >= 3:
                verbose_name = object._meta.get_field(key).verbose_name
                if verbose_name[:4] != key[:4]:
                    new_col_name = f"{keys[0]}.{keys[1]} {verbose_name}"
                else:
                    new_col_name = f"{keys[0]}.{keys[1]} {keys[2]}"
            else:
                new_col_name = key
            if new_col_name not in titles:
                titles.append(new_col_name)
                if key == "II_5_coordonnees":
                    titles += ["lat", "long", "alt", "prec"]
            new_item[new_col_name] = value
        content = list(titles)
        new_item["I. Formulaire"] = viewset.get_view_name()
        new_item["date"] = object.date
        for i, key in enumerate(content):
            value = new_item.get(key)
            if value != None:
                content[i] = new_item.get(key)
            else:
                content[i] = ""
            if key.startswith("II.5"):
                list_coords = new_item.get(key).split()
                new_item["lat"] = list_coords[0]
                new_item["long"] = list_coords[1]
                new_item["alt"] = list_coords[2]
                new_item["prec"] = list_coords[3]
        contents.append(content)
    
print("ENREGISTREMENT")
with open("one_file.csv", "w") as file:
    print("\t".join(titles), file=file)
    for line in tqdm(contents):
        print("\t".join([str(x) if x not in {True, False} else "OUI" if x else "NON" for x in line]), file=file)
