from rds.models.Person import Person as PERSON
from rds.models.Registration import Registration as REG
from rds.models.PersonRegistration import Personregistration as PREG
from voters.models import PersonRegistration
from users.models import UserProfile
from users.types import (
    Gender,MaritalStatus,VotingMethod,VoterType,VotingStatus,
    RegistrationStatus,PendingReason,RejectReason
)
import random
 # 0:reg 1:A5 out 2:A5 in 3:no resp 4:incomplete 5:unknown
        # 6:none 7:reject 8:tidak bisa memilih 9:meninggal 10:pindah dom 11:Ganda 12:DPK 13:testdata
vstats={
    0:'APP',
    1:'A5O',
    2:'A5I',
    4:'PEN',
    7:'REJ',
    8:'NON',
    9:'DEC',
    10:'MOV',
    11:'DUP',
    13:'TEST'

}      
def import_data():
    sudah = MaritalStatus.objects.get(pk=1)
    belum = MaritalStatus.objects.get(pk=2)
    pernah = MaritalStatus.objects.get(pk=3)
    lak_laki = Gender.objects.get(pk=1)
    perempuan = Gender.objects.get(pk=2)
    approve = RegistrationStatus.objects.get(pk=1)
    reject = RegistrationStatus.objects.get(pk=2)
    pending = RegistrationStatus.objects.get(pk=3)
    DPS=VoterType.objects.get(pk=1)
    DPTHP1=VoterType.objects.get(pk=2)
    DPTHP2=VoterType.objects.get(pk=3)
    DPTHP3=VoterType.objects.get(pk=4)
    DPTHP4=VoterType.objects.get(pk=5)
    DPTHP5=VoterType.objects.get(pk=6)
    DPT=VoterType.objects.get(pk=6)
    DPTb=VoterType.objects.get(pk=8)
    DPK=VoterType.objects.get(pk=9)
    TPS=VotingMethod.objects.get(pk=1)
    POS=VotingMethod.objects.get(pk=2)
    NONE=VotingStatus.objects.get(pk=1) 
    CHECKIN=VotingStatus.objects.get(pk=2) 
    SENT=VotingStatus.objects.get(pk=3) 
    RECEIVED=VotingStatus.objects.get(pk=4) 
    RETURNED=VotingStatus.objects.get(pk=5) 
    VOTED = VotingStatus.objects.get(pk=6) 
    LOST = VotingStatus.objects.get(pk=7) 
    R_NONE=RejectReason.objects.get(pk=1)
    NON_CITIZEN=RejectReason.objects.get(pk=2)
    OUT=RejectReason.objects.get(pk=3)
    DUP=RejectReason.objects.get(pk=4)
    UNDER=RejectReason.objects.get(pk=5)
    DECEASED=RejectReason.objects.get(pk=6)
    TEST=RejectReason.objects.get(pk=7)
    P_NONE=PendingReason.objects.get(pk=1)    
    PROOF=PendingReason.objects.get(pk=2)    
    NORESP=PendingReason.objects.get(pk=3)    

    for PR in PREG.objects.using('rds').filter(id__gt = 12007).iterator():
        R = REG.objects.using('rds').filter(id=PR.registration_id).first()
        P = PERSON.objects.using('rds').filter(id = PR.person_id).first()
        email=P.email
        if not P.lastname:
            P.lastname = 'LNU'
        if not email:
            email=f'{P.firstname}_{P.lastname}'
        try:
            UserProfile.objects.get(email=email)
            email=f'{email}_{random.randint(1,100001)}'
        except:
            pass
        print (email,P.firstname,P.lastname)
        if P.gender == 0:
            gender =lak_laki
        else:
            gender =perempuan
        if P.mariagestatus== 1:
            marriage=sudah
        elif P.mariagestatus == 2:
            marriage=pernah
        else: 
            marriage=belum
        user = UserProfile(
            email=email,
            first_name=P.firstname,
            last_name = P.lastname,
            identification=P.identification,
            birthPlace = P.birthplace,
            birthDate = P.birthday,
            address   = P.street,
            city      = P.city,
            state     = P.state,
            zipCode   = P.zipcode,
            telp      = P.telp,
            gender    = gender,
            marital_status  = marriage,
        )
        user.save()
        reject_reason=R_NONE
        pending_reason=P_NONE
        if R.votingmethod == 0:
            voting_method=POS
        else:
            voting_method=TPS

        if PR.votereligible:
            reg_status=approve  #approve 
            voter_type=DPT  #DPT
        else:    
            reg_status=reject   
            voter_type=DPS  
        if R.voterstatus==1:
            reg_status=reject      # Reject
            reject_reason =OUT # Out of Area
        elif R.voterstatus==2:
            reg_status=approve  #approve 
            voter_type=DPTb #DPTb
        elif R.voterstatus==3:
            reg_status=pending      # pending
            pending_reason =NORESP # no response
        elif R.voterstatus==4:
            reg_status=pending      # pending
            pending_reason =PROOF # proof of citizenship
        elif R.voterstatus==5:
            reg_status=pending      # pending
            pending_reason =NORESP # no response
        elif R.voterstatus==6:
            reg_status=pending      # pending
            pending_reason =NORESP # no response
        elif R.voterstatus==7:
            reg_status=reject      # reject
            reject_reason =DUP # duplicate
        elif R.voterstatus==8:
            reg_status=reject      # reject
            reject_reason =NON_CITIZEN  # non citizen
        elif R.voterstatus==9:
            reg_status=reject     # reject
            reject_reason =DECEASED  # Deceased
        elif R.voterstatus==10:
            reg_status=reject      # reject
            reject_reason =OUT  # Out of area
        elif R.voterstatus==11:
            reg_status=reject      # reject
            reject_reason =DUP  # Dup
        elif R.voterstatus==12:
            reg_status=approve      # approve
            voter_type = DPK    # DPK
        elif R.voterstatus==13:
            reg_status=reject      # reject
            reject_reason = TEST    # test data
        voting_status=NONE

        if PR.votingstatus == 4:
            voting_status=SENT # sent
        elif PR.votingstatus == 6:
            voting_status=SENT # sent
        elif PR.votingstatus == 7:
            voting_status=LOST
        elif PR.votingstatus == 3:
            voting_status=CHECKIN
        elif PR.votingstatus == 2:
            voting_status=VOTED
        elif PR.votingstatus == 10:
            voting_status=VOTED

        person_registration = PersonRegistration(
            person=user,
            voter_type = voter_type,
            voting_method = voting_method,
            registration_status = reg_status,
            voting_status = voting_status,
            notes = R.notes,
            registered_time = R.time,
            reject_reason = reject_reason,
            pending_reason = pending_reason,
        ) 
        person_registration.save()
