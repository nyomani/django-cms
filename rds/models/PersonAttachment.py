from django.db import models


class Personattachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    attachement_id = models.BigIntegerField(blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PersonAttachment'
