# Generated by Django 4.2.6 on 2023-11-10 17:01

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascita', models.DateField(blank=True, null=True, verbose_name='Data di Nascita')),
                ('tipo_account', models.CharField(choices=[('admin', 'Admin'), ('developer', 'Developer'), ('cliente', 'Cliente')], max_length=50, verbose_name='Tipologia Utente')),
                ('img_profilo', imagekit.models.fields.ProcessedImageField(default='user_profile/profile_user.png', upload_to='user_profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200, verbose_name='Titolo della slide')),
                ('sottotitolo', models.CharField(blank=True, max_length=250, null=True, verbose_name='Sottotitolo della slide')),
                ('corpo', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Contenuto della slide')),
                ('img', models.ImageField(default='slide/noimg.png', upload_to='slide/%Y/%m/', verbose_name='Immagine Slide')),
                ('pubblicato', models.BooleanField(default=False, verbose_name='Pubblicato')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.carouselcat')),
            ],
        ),
    ]
