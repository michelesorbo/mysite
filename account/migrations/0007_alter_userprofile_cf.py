# Generated by Django 4.2.6 on 2023-11-16 09:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_userprofile_cf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cf',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Inserisci un Codice Fiscale valido', regex='^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$i')], verbose_name='Codice Fiscale'),
        ),
    ]
