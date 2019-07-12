from django.db import models


class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignee = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    referenceid = models.BigIntegerField(db_column='referenceId', blank=True, null=True)  # Field name made lowercase.
    telp = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    useremail = models.CharField(db_column='userEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personregistration_id = models.BigIntegerField(db_column='personRegistration_id', blank=True, null=True)  # Field name made lowercase.
    feedbackstatus = models.IntegerField(db_column='feedbackStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Feedback'
