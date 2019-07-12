from django.db import models


class Configuration(models.Model):
    id = models.BigAutoField(primary_key=True)
    acceptnewperson = models.TextField(db_column='acceptNewPerson', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Configuration'
