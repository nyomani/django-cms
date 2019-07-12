from django.db import models


class Registrationlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    registration_id = models.BigIntegerField(blank=True, null=True)
    votingstatus = models.IntegerField(db_column='votingStatus', blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RegistrationLog'
