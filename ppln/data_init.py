from users.types import (Gender,MaritalStatus,
                         IdentificationType,
                         DisabilityType,
                         VoterType,VotingMethod,VotingStatus,
                         RegistrationStatus,RejectReason,PendingReason
                        )
from django.contrib.auth.models import Group
from ppln.models import(
    Party,Candidate,ElectionType,Team
)                        

def init_gender():
    Gender.objects.create(code='L',desc='Laki-Laki')
    Gender.objects.create(code='P',desc='Perempuan')

def init_marital_status():
    MaritalStatus.objects.create(code='S',desc='Sudah')
    MaritalStatus.objects.create(code='B',desc='Belum')
    MaritalStatus.objects.create(code='P',desc='Pernah')

def init_identification_type():
    IdentificationType.objects.create(desc="PASSPORT")
    IdentificationType.objects.create(desc="EKTP")
    IdentificationType.objects.create(desc="SPLP")

def init_disability_type():
    DisabilityType.objects.create(code='NA',desc='NA')

def init_voter_type():
    VoterType.objects.create(code='DPS',desc='Daftar Pemilih Sementara')
    VoterType.objects.create(code='DPTHP1',desc='Daftar Pemilih Tetap Hasil Perbaikan 1')
    VoterType.objects.create(code='DPTHP2',desc='Daftar Pemilih Tetap Hasil Perbaikan 1')
    VoterType.objects.create(code='DPTHP3',desc='Daftar Pemilih Tetap Hasil Perbaikan 1')
    VoterType.objects.create(code='DPTHP4',desc='Daftar Pemilih Tetap Hasil Perbaikan 1')
    VoterType.objects.create(code='DPTHP5',desc='Daftar Pemilih Tetap Hasil Perbaikan 1')
    VoterType.objects.create(code='DPT',desc='Daftar Pemilih Tetap')
    VoterType.objects.create(code='DPTb',desc='Daftar Pemilih Tetap Tambahan')
    VoterType.objects.create(code='DPK',desc='Daftar Pemilih Khusus')
    VoterType.objects.create(code='Test',desc='Test Data')
def init_votingMethod():
    VotingMethod.objects.create(code='T',desc='TPS')
    VotingMethod.objects.create(code='P',desc='POS')
def init_voting_status():
    VotingStatus.objects.create(code='N',desc='None') 
    VotingStatus.objects.create(code='C',desc='Check in TPS') 
    VotingStatus.objects.create(code='S',desc='Ballot Sent') 
    VotingStatus.objects.create(code='R',desc='Ballot Received') 
    VotingStatus.objects.create(code='RT',desc='Returned to sender') 
    VotingStatus.objects.create(code='V',desc='Voted') 
    VotingStatus.objects.create(code='L',desc='Lost') 
def init_registration_status():
    RegistrationStatus.objects.create(code='A',desc='Approved')
    RegistrationStatus.objects.create(code='R',desc='Reject')
    RegistrationStatus.objects.create(code='P',desc='Pending')
def init_reject_reason():
    RejectReason.objects.create(desc='None')
    RejectReason.objects.create(desc='Non Citizen')
    RejectReason.objects.create(desc='Out of area')
    RejectReason.objects.create(desc='Duplicate')
    RejectReason.objects.create(desc='Under Age')
    RejectReason.objects.create(desc='Deceased')
    RejectReason.objects.create(desc='Test data')
def init_pending_reason():
    PendingReason.objects.create(desc='None')    
    PendingReason.objects.create(desc='Proof of citizenship')    
    PendingReason.objects.create(desc='No Response')    
def init_group():
    Group.objects.create(name='Voter')
    Group.objects.create(name='PPLN')
    Group.objects.create(name='SEKRETARIAT')
    Group.objects.create(name='PANTARLIH')
    Group.objects.create(name='KPPSLN POS')
    Group.objects.create(name='KPPSLN TPS')

def init_election_type():
    ElectionType.objects.create(code='PPWP',description='PPWP')
    ElectionType.objects.create(code='DPR',description='DPR')
