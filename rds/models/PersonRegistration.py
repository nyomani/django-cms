from django.db import models


class Personregistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    registration_id = models.BigIntegerField(blank=True, null=True)
    votereligible = models.TextField(db_column='voterEligible', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    votingstatus = models.IntegerField(db_column='votingStatus', blank=True, null=True)  # Field name made lowercase.
    votingtime = models.DateTimeField(db_column='votingTime', blank=True, null=True)  # Field name made lowercase.
    trackingnumber = models.CharField(db_column='trackingNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    sscount = models.IntegerField(db_column='ssCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonRegistration'
