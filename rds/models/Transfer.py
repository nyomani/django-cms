from django.db import models


class Transfer(models.Model):
    id = models.BigAutoField(primary_key=True)
    destinationcity = models.CharField(db_column='destinationCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationstate = models.CharField(db_column='destinationState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destinationtps = models.CharField(db_column='destinationTPS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    person = models.TextField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Transfer'
