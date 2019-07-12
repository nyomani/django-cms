from django.db import models


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    articleindex = models.IntegerField(db_column='articleIndex', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='dateCreated', blank=True, null=True)  # Field name made lowercase.
    icon = models.IntegerField(blank=True, null=True)
    lastupdateddate = models.DateTimeField(db_column='lastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    metadata_id = models.BigIntegerField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Article'
