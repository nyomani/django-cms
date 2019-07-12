from django.db import models


class Login(models.Model):
    id = models.BigAutoField(primary_key=True)
    accountexpired = models.TextField(db_column='accountExpired', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    locked = models.TextField(blank=True, null=True)  # This field type is a guess.
    password = models.CharField(max_length=255, blank=True, null=True)
    passwordexpired = models.TextField(db_column='passwordExpired', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    time = models.DateTimeField(blank=True, null=True)
    userid = models.CharField(db_column='userId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertype = models.IntegerField(db_column='userType', blank=True, null=True)  # Field name made lowercase.
    person_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Login'
