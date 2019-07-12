from django.db import models


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoryindex = models.IntegerField(db_column='categoryIndex', blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'
