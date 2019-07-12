from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models import CMSPlugin
from users.models import UserProfile
from users.types import (
    VotingMethod,VoterType,
    VotingStatus,RegistrationStatus,
    PendingReason,RejectReason
)
from django.utils.timezone import now
class PersonRegistration(models.Model):
    person=models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True,)
    voting_method = models.ForeignKey(VotingMethod,on_delete=models.CASCADE,default=1)
    registration_status = models.ForeignKey(RegistrationStatus,on_delete=models.CASCADE,default=1)
    registered_time = models.DateTimeField(default=now,editable=False)
    voting_status = models.ForeignKey(VotingStatus,on_delete=models.CASCADE,default=1)
    voter_type = models.ForeignKey(VoterType,on_delete=models.CASCADE,default=1)
    reject_reason = models.ForeignKey(RejectReason,on_delete=models.CASCADE,null=True,blank=True)
    pending_reason = models.ForeignKey(PendingReason,on_delete=models.CASCADE,null=True,blank=True)
    notes = HTMLField('Notes',null=True,blank=True)

    def first_name(self):
        return self.person.first_name
    def last_name(self):
        return self.person.last_name
    def follow_up_needed(self):
        if  self.registration_status == 2 :
            return True
        return False
    def voter_status_msg(self):
        if  self.registration_status.code == 'P':
            return 'Status PENDING. Please contact PPLN Chicago to complete your registration'
        elif self.registration_status.code=='R':
            return f'Not eligible to vote due to { self.reject_reason}'
        elif self.voting_status.code == 'V':
                if self.voting_method.code=='P':
                    return 'Voted by POS'
                else:
                    return 'Vote at TPS'
        else: 
            return f'Voting status  {self.voting_status}'
