from django.db import models


class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.CharField(max_length=512, blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    referenceid = models.BigIntegerField(db_column='referenceId', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    attacment_id = models.BigIntegerField(blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Message'
