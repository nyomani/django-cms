from django.db import models


class Transferrequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    destinationcity = models.CharField(db_column='destinationCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationstate = models.CharField(db_column='destinationState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationtps = models.CharField(db_column='destinationTPS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    destinationkecamatan = models.CharField(db_column='destinationKecamatan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationppln = models.CharField(db_column='destinationPPLN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationtpsln = models.CharField(db_column='destinationTPSLN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationkjri = models.CharField(db_column='destinationKJRI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransferRequest'
