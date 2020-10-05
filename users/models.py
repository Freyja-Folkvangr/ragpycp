from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class CustomUserManager(UserManager):
    pass

class Login(AbstractUser):
    SEX = (
        ('M', '👦🏻'),
        ('F', '👧🏻')
    )
    STATES = (
        (0, 'Active'),
        (1, 'Banned')
    )
    id = models.AutoField(primary_key=True, db_column='account_id', verbose_name='Account ID')
    username = models.CharField(unique=True, max_length=23, db_column='userid')
    password = models.CharField(max_length=32, db_column='user_pass')
    sex = models.CharField(choices=SEX, max_length=1, verbose_name='Gender', default='F')
    email = models.CharField(unique=True, max_length=39)
    group_id = models.IntegerField(default=0, null=False, blank=False)
    state = models.PositiveIntegerField(choices=STATES, default=0, null=False, verbose_name='RO State')
    unban_time = models.PositiveIntegerField(null=False, blank=True, default=0)
    expiration_time = models.PositiveIntegerField(null=False, blank=True, default=0)
    logincount = models.PositiveIntegerField(default=0, blank=True)
    last_login = models.DateTimeField(blank=True, null=True, db_column='lastlogin')
    last_ip = models.CharField(max_length=100, null=False, blank=True)
    birthdate = models.DateField(null=True, blank=True, default='2019-05-19')
    character_slots = models.PositiveIntegerField(null=False, blank=False, default=12)
    pincode = models.CharField(max_length=4, null=False, blank=True)
    pincode_change = models.PositiveIntegerField(default=0, blank=True)
    vip_time = models.PositiveIntegerField(null=False, blank=True, default=0)
    old_group = models.IntegerField(null=False, blank=True, default=0)
    web_auth_token = models.CharField(unique=True, max_length=17, blank=True, null=True, default=None)
    web_auth_token_enabled = models.IntegerField(default=0)

    @property
    def state_str(self):
        return self.STATES[self.state][1]

    def __str__(self):
        return '[%s] %s (%s)' % (self.id, self.username, self.state_str)

    class Meta:
        managed = True
        db_table = 'login'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    objects = CustomUserManager()

# This model is used for installation
class Login2(models.Model):
    account_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=23)
    user_pass = models.CharField(max_length=32)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=39)
    group_id = models.IntegerField()
    state = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    expiration_time = models.PositiveIntegerField()
    logincount = models.PositiveIntegerField()
    lastlogin = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    character_slots = models.PositiveIntegerField()
    pincode = models.CharField(max_length=4)
    pincode_change = models.PositiveIntegerField()
    vip_time = models.PositiveIntegerField()
    old_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login2'