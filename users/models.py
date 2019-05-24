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
    group_id = models.IntegerField(default=0, null=False)
    state = models.PositiveIntegerField(choices=STATES, default=0, null=False, verbose_name='RO State')
    unban_time = models.PositiveIntegerField(null=True, blank=True)
    expiration_time = models.PositiveIntegerField(null=True, blank=True)
    logincount = models.PositiveIntegerField(default=0, blank=True)
    last_login = models.DateTimeField(blank=True, null=True, db_column='lastlogin')
    last_ip = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True, default='2019-05-19')
    character_slots = models.PositiveIntegerField(null=True, blank=True)
    pincode = models.CharField(max_length=4, null=True, blank=True)
    pincode_change = models.PositiveIntegerField(default=0)
    vip_time = models.PositiveIntegerField(null=True, blank=True)
    old_group = models.IntegerField(null=True, blank=True)

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