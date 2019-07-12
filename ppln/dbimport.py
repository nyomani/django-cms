from rds.models.Person import Person as PERSON
from rds.models.Party import Party as PRTY
from rds.models.Tally  import Tally
from ppln.models import Party,ElectionType,Candidate
from django.core.exceptions import ObjectDoesNotExist

def import_candidate():
    for t in Tally.objects.using('rds').all().iterator():
        print('{} {}'.format(t.name,t.party_id))
        try:
            prty = PRTY.objects.using('rds').get(partyid=t.party_id)
            try:
                party = Party.objects.get(party_id=prty.partyid) or None
            except ObjectDoesNotExist:
                party = Party(party_id=prty.partyid,description=prty.name)
                party.save()
                print('Party does not exist create one ',prty.partyid,prty.name)
        except ObjectDoesNotExist:
            try:
                party = Party.objects.get(party_id=t.party_id) or None
            except ObjectDoesNotExist:
                party = Party(party_id=t.party_id,description="Unknown")
                party.save()
                print('Party does not exist create one ',party.id,party.description)
        if t.votingtype==0:
            e_type=ElectionType.objects.get(code='PPWP')
        else:
            e_type=ElectionType.objects.get(code='DPR')
        print(e_type)
        candidate = Candidate(party=party,
                            election_type=e_type,
                            candidate_id=t.sequenceid,
                            name=t.name,
                            vote_count_tps=t.tpscount,
                            vote_count_pos =t.postcount
                            )
        candidate.save()
