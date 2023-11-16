# Generated by Django 4.2.6 on 2023-11-13 08:37

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userprofile_img_profilo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img_profilo',
            field=imagekit.models.fields.ProcessedImageField(default='user_profile/profile_user.png', upload_to='user_profile/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tipo_account',
            field=models.CharField(choices=[('admin', 'Admin'), ('developer', 'Developer'), ('cliente', 'Cliente')], default='cliente', max_length=50, verbose_name='Tipologia Utente'),
        ),
    ]
