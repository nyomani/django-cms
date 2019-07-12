from django.db import models


class Documentmetadata(models.Model):
    id = models.BigAutoField(primary_key=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mimetype = models.CharField(db_column='mimeType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocumentMetaData'
