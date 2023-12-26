import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AmatembarubingoServer.settings")

import django
django.setup()

from api.models import Province, Commune, Colline
from tqdm import tqdm
import json

with open("burundizipcode.txt", "r") as file:
    for str_line in tqdm(file.readlines()):
        line = json.loads(str_line)
        province,_ = Province.objects.get_or_create(nom=line[1])
        commune,_ = Commune.objects.get_or_create(
            province = province, nom=line[2]
        )
        colline,_ = Colline.objects.get_or_create(commune=commune, nom=line[3], id=line[0])