from django.contrib import admin
from LogBook.models import MycsvModel


class IcaoAirportDisplay(admin.ModelAdmin):
    list_display = ("ident","name", "type", "name", "latitude_deg",
                    "longitude_deg", "elevation_ft", "continent",
                    "iso_country", "iso_region", "municipality",
                    "gps_code", "iata_code", "local_code")

     # list_filter = ("ident","name","iata_code")
    search_fields = ("name","ident")

admin.site.register(MycsvModel,IcaoAirportDisplay)

