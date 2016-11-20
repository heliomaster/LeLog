import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand
# from src.essaiCsv.models import MycsvModel
from LogBook.models import MycsvModel


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = os.path.join(settings.BASE_DIR, "airportCodes.csv")
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row)
            obj = MycsvModel.objects.create(
                ident=row['ident'],
                type=row['type'],
                name=row['name'],
                latitude_deg=row['latitude_deg'],
                longitude_deg=row['longitude_deg'],
                elevation_ft=row['elevation_ft'],
                continent=row['continent'],
                iso_country=row['iso_country'],
                iso_region=row['iso_region'],
                municipality=row["municipality"],
                gps_code=row["gps_code"],
                iata_code=row["iata_code"],
                local_code=row["local_code"],
                 )
            print(obj)
