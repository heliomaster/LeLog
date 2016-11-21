from django.db import models


class Logfields(models.Model):
    Date_field = models.DateTimeField()

    off_block_time = models.TimeField()
    take_off_time = models.TimeField()
    land_time = models.TimeField
    on_block_time = models.TimeField()
    tot_time_field = models.TimeField()

    pic_field = models.CharField(max_length=50)
    fo_field = models.CharField(max_length=50)
# related_name: for foreignkey
    dep_field = models.ForeignKey('MycsvModel', on_delete=models.CASCADE, related_name="dep_field")
    arrival_field = models.ForeignKey('MycsvModel', on_delete=models.CASCADE, related_name="arrival_field")


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


    Day_or_Night = (
        ("D", "Day"),
        ("N", "Night")
    )
    conditions = models.CharField(
        max_length=1,
        choices=Day_or_Night,
        default="?"
    )

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.ident
