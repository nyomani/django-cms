from django.db import models

class PendingReason(models.Model):
    desc = models.CharField(max_length=32)
    def __str__(self):
        return self.desc

class RejectReason(models.Model):
    desc = models.CharField(max_length=32)
    def __str__(self):
        return self.desc

class IdentificationType(models.Model):
    desc = models.CharField(max_length=16,default='PASSPORT')
    def __str__(self):
        return self.desc

class Gender(models.Model):
    code = models.CharField(max_length=1,default='M')
    desc = models.CharField(max_length=16,default='Male')
    def __str__(self):
        return self.desc

class MaritalStatus(models.Model):
    code = models.CharField(max_length=1,default='M')
    desc = models.CharField(max_length=16,default='Married')
    def __str__(self):
        return self.desc

class DisabilityType(models.Model):
    code = models.CharField(max_length=2,default='NA')
    desc = models.CharField(max_length=32,default='NA')
    def __str__(self):
        return self.desc

class VotingMethod(models.Model):
    code = models.CharField(max_length=1,default='T')
    desc = models.CharField(max_length=32,default='TPS')
    def __str__(self):
        return self.desc

class VoterType(models.Model):
    code = models.CharField(max_length=6,default='DPS')
    desc = models.CharField(max_length=64,default='Daftar Pemilih Sementara')
    def __str__(self):
        return self.desc

class RegistrationStatus(models.Model):
    code = models.CharField(max_length=6,default='APP')
    desc = models.CharField(max_length=64,default='Approved')
    def __str__(self):
        return self.desc

class VotingStatus(models.Model):
    code = models.CharField(max_length=6,default='N')
    desc = models.CharField(max_length=64,default='None')
    def __str__(self):
        return self.desc

