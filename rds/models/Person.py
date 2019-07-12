from django.db import models


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    birthplace = models.CharField(db_column='birthPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    createdtime = models.DateTimeField(db_column='createdTime', blank=True, null=True)  # Field name made lowercase.
    disabilitytype = models.CharField(db_column='disabilityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(blank=True, null=True)
    identification = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='lastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    mariagestatus = models.IntegerField(db_column='mariageStatus', blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    referenceid = models.BigIntegerField(db_column='referenceId', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    telp = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(db_column='zipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return '{} {}'.format(self.firstname,self.lastname)
    class Meta:
        managed = False
        db_table = 'Person'
