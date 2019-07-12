from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager as DjangoBaseUserManager
from django.utils import timezone
from phone_field import PhoneField
from .types import (
    IdentificationType,Gender,MaritalStatus,
    VoterType,VotingMethod,VotingStatus,
    RegistrationStatus,DisabilityType
)

class BaseUserManager(DjangoBaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class UserProfile(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    identification=models.CharField(max_length=64,null=True,blank=True)
    id_type    = models.ForeignKey(IdentificationType,default=1,on_delete=models.CASCADE)
    birthPlace = models.CharField(max_length=32,null=True,blank=True)
    birthDate = models.DateField(null=True)
    address   = models.CharField(max_length=64,null=True,blank=True)
    city      = models.CharField(max_length=32,null=True,blank=True)
    state     = models.CharField(max_length=3,null=True,blank=True)
    zipCode   = models.CharField(max_length=16,null=True,blank=True)
    telp      = PhoneField(blank=True,null=True,help_text='Contact phone number')
    gender    = models.ForeignKey(Gender,default=1,on_delete=models.CASCADE)
    marital_status  = models.ForeignKey(MaritalStatus,default=1,on_delete=models.CASCADE)
    disability = models.ForeignKey(DisabilityType,default=1,on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = BaseUserManager()
