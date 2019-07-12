from django.db import models


class Tpsvoting(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TPSVoting'
