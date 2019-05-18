from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class CustomUserManager(UserManager):
    pass

class Login(AbstractUser):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    id = models.AutoField(primary_key=True, name='account_id')
    username = models.CharField(unique=True, max_length=23, name='userid')
    password = models.CharField(max_length=32, name='user_pass')
    sex = models.CharField(choices=SEX, max_length=1)
    email = models.CharField(unique=True, max_length=39)
    group_id = models.IntegerField(default=0, null=False)
    state = models.PositiveIntegerField(default=0, null=False)
    unban_time = models.PositiveIntegerField(null=True)
    expiration_time = models.PositiveIntegerField(null=True)
    logincount = models.PositiveIntegerField(default=0)
    last_login = models.DateTimeField(blank=True, null=True, name='lastlogin')
    last_ip = models.CharField(max_length=100, null=True)
    birthdate = models.DateField(null=True)
    character_slots = models.PositiveIntegerField(null=True)
    pincode = models.CharField(max_length=4, null=True)
    pincode_change = models.PositiveIntegerField(default=0)
    vip_time = models.PositiveIntegerField(null=True)
    old_group = models.IntegerField(null=True)

    class Meta:
        managed = True
        db_table = 'login'

    objects = CustomUserManager()