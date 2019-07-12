from django.db import models


class Registration(models.Model):
    id = models.BigAutoField(primary_key=True)
    approvalcode = models.CharField(db_column='approvalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approvalstatus = models.IntegerField(db_column='approvalStatus', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    userconfirmation = models.IntegerField(db_column='userConfirmation', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    voterstatus = models.IntegerField(db_column='voterStatus', blank=True, null=True)  # Field name made lowercase.
    votingmethod = models.IntegerField(db_column='votingMethod', blank=True, null=True)  # Field name made lowercase.
    registrationstatus = models.IntegerField(db_column='registrationStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Registration'
