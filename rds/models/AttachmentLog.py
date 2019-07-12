from django.db import models


class Attachmentlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    document_id = models.BigIntegerField(blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AttachmentLog'
