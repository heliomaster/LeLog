from django.contrib import admin
from .forms import LogfieldsForm
from LogBook.models import MycsvModel
from LogBook.models import Logfields

"""Le fichier admin.py sert à manager l'interface d'admin"""


# creation d'un champ LogfieldsDisplay apparaissant dans l'affichage d'admin
# ATT: form=LogfieldsForm est importé de forms.py(où toutes les forms sont mises
# ne pas oublier de registrer tous à la fin avec admin.register etc...

# list_display == affichage du titre DIFF de celui dans forms qui lui permet des modifs
class LogfieldsDisplay(admin.ModelAdmin):
    # __str__ pour afficher ds admin le model date/time qui des integers au depart
    list_display = ("__str__", "dep_field", "arrival_field")
    form = LogfieldsForm




class IcaoAirportDisplay(admin.ModelAdmin):
    list_display = ("ident", "name", "type", "name", "latitude_deg",
                    "longitude_deg", "elevation_ft", "continent",
                    "iso_country", "iso_region", "municipality",
                    "gps_code", "iata_code", "local_code")

# list_filter = ("ident","name","iata_code")
    search_fields = ("name", "ident")

admin.site.register(MycsvModel, IcaoAirportDisplay)
admin.site.register(Logfields, LogfieldsDisplay)
