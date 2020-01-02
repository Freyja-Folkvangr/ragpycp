from django.db import models
from users.models import Login

# Create your models here.

JOBS = (
    (0, 'Novice'),
    (1, 'Swordman'),
    (2, 'Magician'),
    (3, 'Archer'),
    (4, 'Acolyte'),
    (5, 'Merchant'),
    (6, 'Thief'),
    (7, 'Knight'),
    (8, 'Priest'),
    (9, 'Wizard'),
    (10, 'Blacksmith'),
    (11, 'Hunter'),
    (12, 'Assassin'),
    (13, 'Knight (Peco)'),
    (14, 'Crusader'),
    (15, 'Monk'),
    (16, 'Sage'),
    (17, 'Rogue'),
    (18, 'Alchemist'),
    (19, 'Bard'),
    (20, 'Dancer'),
    (21, 'Crusader (Peco)'),
    (22, 'Wedding (Deprecated)'),
    (23, 'Super Novice'),
    (24, 'Gunslinger'),
    (25, 'Ninja'),
    (4001, 'Novice High'),
    (4002, 'Swordman High'),
    (4003, 'Magician High'),
    (4004, 'Archer High'),
    (4005, 'Acolyte High'),
    (4006, 'Merchant High'),
    (4007, 'Thief High'),
    (4008, 'Lord Knight'),
    (4009, 'High Priest'),
    (4010, 'High Wizard'),
    (4011, 'Whitesmith'),
    (4012, 'Sniper'),
    (4013, 'Assassin Cross'),
    (4014, 'Lord Knight (Peco)'),
    (4015, 'Paladin'),
    (4016, 'Champion'),
    (4017, 'Professor'),
    (4018, 'Stalker'),
    (4019, 'Creator'),
    (4020, 'Clown'),
    (4021, 'Gypsy'),
    (4022, 'Paladin (Peco)'),
    (4023, 'Baby Novice'),
    (4024, 'Baby Swordman'),
    (4025, 'Baby Magician'),
    (4026, 'Baby Archer'),
    (4027, 'Baby Acolyte'),
    (4028, 'Baby Merchant'),
    (4029, 'Baby Thief'),
    (4030, 'Baby Knight'),
    (4031, 'Baby Priest'),
    (4032, 'Baby Wizard'),
    (4033, 'Baby Blacksmith'),
    (4034, 'Baby Hunter'),
    (4035, 'Baby Assassin'),
    (4036, 'Baby Knight (Peco)'),
    (4037, 'Baby Crusader'),
    (4038, 'Baby Monk'),
    (4039, 'Baby Sage'),
    (4040, 'Baby Rogue'),
    (4041, 'Baby Alchemist'),
    (4042, 'Baby Bard'),
    (4043, 'Baby Dancer'),
    (4044, 'Baby Crusader (Peco)'),
    (4045, 'Baby Super Novice'),
    (4046, 'Taekwon'),
    (4047, 'Star Gladiator'),
    (4048, 'Star Gladiator (Union)'),
    (4049, 'Soul Linker'),
    (4050, 'Gangsi (Bongun/Munak)'),
    (4051, 'Death Knight'),
    (4052, 'Dark Collector'),
    (4054, 'Rune Knight (Regular)'),
    (4055, 'Warlock (Regular)'),
    (4056, 'Ranger (Regular)'),
    (4057, 'Arch Bishop (Regular)'),
    (4058, 'Mechanic (Regular)'),
    (4059, 'Guillotine Cross (Regular)'),
    (4060, 'Rune Knight (Trans)'),
    (4061, 'Warlock (Trans)'),
    (4062, 'Ranger (Trans)'),
    (4063, 'Arch Bishop (Trans)'),
    (4064, 'Mechanic (Trans)'),
    (4065, 'Guillotine Cross (Trans)'),
    (4066, 'Royal Guard (Regular)'),
    (4067, 'Sorcerer (Regular)'),
    (4068, 'Minstrel (Regular)'),
    (4069, 'Wanderer (Regular)'),
    (4070, 'Sura (Regular)'),
    (4071, 'Genetic (Regular)'),
    (4072, 'Shadow Chaser (Regular)'),
    (4073, 'Royal Guard (Trnas)'),
    (4074, 'Sorcerer (Trans)'),
    (4075, 'Minstrel (Trans)'),
    (4076, 'Wanderer (Trans)'),
    (4077, 'Sura (Trans)'),
    (4078, 'Genetic (Trans)'),
    (4079, 'Shadow Chaser (Trans)'),
    (4080, 'Rune Knight (Dragon) (Regular)'),
    (4081, 'Rune Knight (Dragon) (Trans)'),
    (4082, 'Royal Guard (Gryphon) (Regular)'),
    (4083, 'Royal Guard (Gryphon) (Trans)'),
    (4084, 'Ranger (Warg) (Regular)'),
    (4085, 'Ranger (Warg) (Trans)'),
    (4086, 'Mechanic (Mado) (Regular)'),
    (4087, 'Mechanic (Mado) (Trans)'),
    (4096, 'Baby Rune Knight'),
    (4097, 'Baby Warlock'),
    (4098, 'Baby Ranger'),
    (4099, 'Baby Arch Bishop'),
    (4100, 'Baby Mechanic'),
    (4101, 'Baby Guillotine Cross'),
    (4102, 'Baby Royal Guard'),
    (4103, 'Baby Sorcerer'),
    (4104, 'Baby Minstrel'),
    (4105, 'Baby Wanderer'),
    (4106, 'Baby Sura'),
    (4107, 'Baby Genetic'),
    (4108, 'Baby Shadow Chaser'),
    (4109, 'Baby Rune Knight (Dragon)'),
    (4110, 'Baby Royal Guard (Gryphon)'),
    (4111, 'Baby Ranger (Warg)'),
    (4112, 'Baby Mechanic (Mado)'),
    (4190, 'Super Novice (Expanded)'),
    (4191, 'Super Baby (Expanded)'),
    (4211, 'Kagerou'),
    (4212, 'Oboro'),
    (4215, 'Rebellion'),
    (4218, 'Summoner'),
    (4220, 'Baby Summoner'),
    (4222, 'Baby Ninja'),
    (4223, 'Baby Kagerou'),
    (4224, 'Baby Oboro'),
    (4225, 'Baby Taekwon'),
    (4226, 'Baby Star Gladiator'),
    (4227, 'Baby Soul Linker'),
    (4228, 'Baby Gunslinger'),
    (4229, 'Baby Rebellion'),
    (4238, 'Baby Star Gladiator (Union)'),
    (4239, 'Star Emperor'),
    (4240, 'Soul Reaper'),
    (4241, 'Baby Star Emperor'),
    (4242, 'Baby Soul Reaper'),
    (4243, 'Star Emperor (Union)'),
    (4244, 'Baby Star Emperor (Union)')
)


class Char(models.Model):
    char_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(Login, on_delete=models.CASCADE, db_column='account_id')
    char_num = models.IntegerField()
    name = models.CharField(unique=True, max_length=30)
    class_field = models.PositiveSmallIntegerField(choices=JOBS, db_column='class',
                                                   help_text='Do not change manually, use in-game commands instead.')  # Field renamed because it was a Python reserved word.
    base_level = models.PositiveSmallIntegerField()
    job_level = models.PositiveSmallIntegerField()
    base_exp = models.BigIntegerField()
    job_exp = models.BigIntegerField()
    zeny = models.PositiveIntegerField()
    str = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    luk = models.PositiveSmallIntegerField()
    max_hp = models.PositiveIntegerField()
    hp = models.PositiveIntegerField()
    max_sp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    status_point = models.PositiveIntegerField()
    skill_point = models.PositiveIntegerField()
    option = models.IntegerField()
    karma = models.IntegerField()
    manner = models.SmallIntegerField()
    party_id = models.PositiveIntegerField()
    guild_id = models.PositiveIntegerField()
    pet_id = models.PositiveIntegerField()
    homun_id = models.PositiveIntegerField()
    elemental_id = models.PositiveIntegerField()
    hair = models.PositiveIntegerField()
    hair_color = models.PositiveSmallIntegerField()
    clothes_color = models.PositiveSmallIntegerField()
    body = models.PositiveSmallIntegerField()
    weapon = models.PositiveSmallIntegerField()
    shield = models.PositiveSmallIntegerField()
    head_top = models.PositiveSmallIntegerField()
    head_mid = models.PositiveSmallIntegerField()
    head_bottom = models.PositiveSmallIntegerField()
    robe = models.PositiveSmallIntegerField()
    last_map = models.CharField(max_length=11)
    last_x = models.PositiveSmallIntegerField()
    last_y = models.PositiveSmallIntegerField()
    save_map = models.CharField(max_length=11)
    save_x = models.PositiveSmallIntegerField()
    save_y = models.PositiveSmallIntegerField()
    partner_id = models.PositiveIntegerField()
    online = models.IntegerField()
    father = models.PositiveIntegerField()
    mother = models.PositiveIntegerField()
    child = models.PositiveIntegerField()
    fame = models.PositiveIntegerField()
    rename = models.PositiveSmallIntegerField()
    delete_date = models.PositiveIntegerField()
    moves = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    font = models.PositiveIntegerField()
    uniqueitem_counter = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    hotkey_rowshift = models.PositiveIntegerField()
    clan_id = models.PositiveIntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    title_id = models.PositiveIntegerField()
    show_equip = models.PositiveIntegerField()

    def __str__(self):
        return '%s [%s - %s/%s]' % (self.name.upper(), self.get_job_name(), self.base_level, self.job_level)

    def get_job_name(self):
        for item in JOBS:
            if item[0] == self.class_field:
                return item[1]
        return 'unknown'

    def reset_position(self):
        self.last_map = 'prontera'
        self.last_x = 160
        self.last_y = 160
        return self.save()

    def reset_save_position(self):
        self.save_map = 'prontera'
        self.save_x = 160
        self.save_y = 160
        return self.save()

    def reset_appearance(self):
        self.hair = 1
        self.hair_color = 1
        self.clothes_color = 1
        return self.save()

    class Meta:
        managed = False
        db_table = 'char'
