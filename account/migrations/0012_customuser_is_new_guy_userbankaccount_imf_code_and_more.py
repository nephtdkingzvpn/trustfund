# Generated by Django 4.2.3 on 2025-04-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_userbankaccount_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_new_guy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userbankaccount',
            name='imf_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userbankaccount',
            name='transfer_otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
