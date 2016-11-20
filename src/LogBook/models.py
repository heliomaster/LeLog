from django.db import models


class MycsvModel(models.Model):
    ident = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    latitude_deg = models.FloatField(null=True, blank=True)
    longitude_deg = models.FloatField(null=True, blank=True)
    elevation_ft = models.CharField(max_length=200, null=True, blank=True)
    continent = models.CharField(max_length=200, null=True, blank=True)
    iso_country = models.CharField(max_length=200, null=True, blank=True)
    iso_region = models.CharField(max_length=200, null=True, blank=True)
    municipality = models.CharField(max_length=200, null=True, blank=True)
    gps_code = models.CharField(max_length=200, null=True, blank=True)
    iata_code = models.CharField(max_length=200, null=True, blank=True)
    local_code = models.CharField(max_length=200, null=True, blank=True)




    def __str__(self):
        return self.ident
