from django.db import models


class Party(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    partyid = models.BigIntegerField(db_column='partyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Party'
