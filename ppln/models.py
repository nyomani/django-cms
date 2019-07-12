from django.db import models
from django.contrib.auth.models import Group
from djangocms_text_ckeditor.fields import HTMLField
from django.utils import timezone
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from cms.models import CMSPlugin
from users.models import UserProfile
from cms.forms.fields import PageSelectFormField
from cms.extensions.extension_pool import extension_pool
from .page import MetaPage


class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')

extension_pool.register(IconExtension)

class ElectionType(models.Model):
    code= models.CharField(max_length=6)
    description= models.CharField(max_length=16)
    def __str__(self):
        return self.description

class Party(models.Model):
    image = models.ImageField(upload_to='icons',null=True)
    party_id=models.IntegerField(default=0)
    code= models.CharField(max_length=6,null=True)
    description= models.CharField(max_length=64)
    def __str__(self):
        return '{}{}{}'.format(self.party_id,'. ',self.description)

class Candidate(models.Model):
    image = models.ImageField(upload_to='icons',null=True)
    party = models.ForeignKey(Party,on_delete=models.CASCADE)
    election_type = models.ForeignKey(ElectionType,default=1,
                on_delete=models.CASCADE,
                help_text="Election Types")
    candidate_id = models.IntegerField(default=0)
    name = models.CharField(max_length=64)
    vote_count = models.IntegerField(default=0)
    vote_count_tps=models.IntegerField(default=0)
    vote_count_pos=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class PresidentailTallyPluginModel(CMSPlugin):
    def __str__(self):
        return "PPWP"
class ParliamentTallyPluginModel(CMSPlugin):
    def __str__(self):
        return "DPR"       
class Team(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,null=True)
    rank = models.IntegerField(default=1)
    description = HTMLField(null=True,blank=True)

    def __str__(self):
        return f'{self.profile.first_name} {self.profile.last_name}'

class TeamPluginModel(CMSPlugin):
    user_group = models.ForeignKey(Group,on_delete=models.CASCADE)
    title = HTMLField(null=True,blank=True)
    def __str__(self):
        return self.user_group.name


task_status=[
    ("UNKN","Unknown"),
    ("INP","In Progress"),
    ("PEN","Pending"),
    ("COMP","Completed"),
    ("CNCL","Canceled"),
]

class TaskType(models.Model):
    task_type = models.CharField(max_length=64)

    def __str__(self):
        return self.task_type

class Task(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType,on_delete=models.CASCADE)
    due_date = models.DateField()
    completion_date=models.DateField(null=True,blank=True)
    status = models.CharField(max_length=16,
                            choices=task_status,
                            default="UNKN")
    auth_code=models.CharField(max_length=256,null=True,blank=True)

    def __str__(self):
        return self.task_type.task_type

    def forward(self,u):
        self.user = u
    def progressing(self):
        self.status = 'INP'
    def pending(self):
        self.status = 'PEN'
    def completed(self):
        self.status = 'COMP'
        self.completion_date=timezone.now
    def cancel(self):
        self.status = 'CNCL'
extension_pool.register(MetaPage)
