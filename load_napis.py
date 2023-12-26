import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AmatembarubingoServer.settings")

import django
django.setup()

from api.models import Province, Commune, Colline, Zone
from tqdm import tqdm
import json

with open("napis_province.csv", "r") as file:
    for str_line in tqdm(file.readlines()[1:]):
        line = str_line.split(",")
        try:
            if "province" in line[0].lower():
                province,_ = Province.objects.get_or_create(id=line[1], nom=line[2])
            if "commune" in line[0].lower():
                province = Province.objects.get(id=line[3])
                commune,_ = Commune.objects.get_or_create(province = province, id=line[1], nom=line[2])
            if "zone" in line[0].lower():
                commune = Commune.objects.get(id=line[4])
                zone,_ = Zone.objects.get_or_create(commune=commune, id=line[1], nom=line[2])
            if "colline" in line[0].lower():
                zone = Zone.objects.get(id=line[5])
                colline,_ = Colline.objects.get_or_create(zone=zone, id=line[1], nom=line[2])
        except Exception as e:
            print(f"[EXCEPTION] {e} on {line}")