from rds.models.Person import Person as PERSON
from rds.models.Registration import Registration as REG
from rds.models.PersonRegistration import Personregistration as PREG
from voters.models import PersonRegistration
from users.models import UserProfile
from users.types import (
    Gender,MaritalStatus,VotingMethod,VoterType,VotingStatus,
    RegistrationStatus,PendingReason,RejectReason
)
def import_data():
    len(PREG.objects.using('rds').all())

"""     for PR in PREG.objects.using('rds').all().iterator():
        R = REG.objects.using('rds').filter(id=PR.registration_id).first()
        P = PERSON.objects.using('rds').filter(id = PR.person_id).first()
        p = PERSON.objects.create(P)
        r = REG.objects.create(R)
        r.person=p.id
        p.save()
        r.save() """