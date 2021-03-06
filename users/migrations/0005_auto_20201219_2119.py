# Generated by Django 3.0.7 on 2020-12-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_restore_login_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='vip_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='login',
            name='web_auth_token',
            field=models.CharField(default=None, max_length=17, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='web_auth_token_enabled',
            field=models.IntegerField(default=0),
        ),
    ]
