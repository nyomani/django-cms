from django.db import models


class Tally(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sequenceid = models.IntegerField(db_column='sequenceId', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    votingtype = models.IntegerField(db_column='votingType', blank=True, null=True)  # Field name made lowercase.
    party_id = models.BigIntegerField(blank=True, null=True)
    postcount = models.IntegerField(db_column='postCount', blank=True, null=True)  # Field name made lowercase.
    tpscount = models.IntegerField(db_column='tpsCount', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.name,self.type,self.votingtype,self.party_id,self.postcount,self.tpscount)
    class Meta:
        managed = False
        db_table = 'Tally'
