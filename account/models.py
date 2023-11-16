from django.db import models
#Per immagine preview in admin
from django.utils.html import mark_safe

#Resize Image
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToCover

#CK Editor
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#Eliminare le immagini quando si elimina un oggetto
from django_cleanup import cleanup

#Espando User
from django.contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#Importo il validatore con le regole di RecEx
from django.core.validators import RegexValidator

# Create your models here.
#Tabelle per Carosello

class CarouselCat(models.Model):
    nome = models.CharField("Nome Categoria", max_length=150)

    def __str__(self):
        return self.nome

@cleanup.select
class Carousel(models.Model):
    titolo = models.CharField("Titolo della slide", max_length=200)
    sottotitolo = models.CharField("Sottotitolo della slide", max_length=250, blank=True, null=True)
    corpo = RichTextUploadingField("Contenuto della slide", blank=True, null=True)
    #corpo = models.TextField("Contenuto della slide")
    categoria = models.ForeignKey(CarouselCat, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField("Immagine Slide", upload_to='slide/%Y/%m/', default='slide/noimg.png')
    img_resize = ImageSpecField(source='img', processors=[ResizeToCover(800,800)], format='PNG', options={'quality':60})
    pubblicato = models.BooleanField("Pubblicato", default=False)

    def __str__(self):
        return self.titolo
    
    #Per visualizzare immagine in Admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')
    
#Model per Utenti
#Personalizziamo l'account utente
@cleanup.select
class UserProfile(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('developer', 'Developer'),
        ('cliente', 'Cliente')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascita = models.DateField("Data di Nascita", null=True, blank=True)
    cf =  models.CharField("Codice Fiscale", max_length=16, blank=True, null=True, validators=[RegexValidator(
        regex=r'^[A-Za-z]{6}[0-9]{2}[A-Za-z]{1}[0-9]{2}[A-Za-z]{1}[0-9]{3}[A-Za-z]{1}$',
        message='Inserisci un Codice Fiscale valido'
    )])
    tipo_account = models.CharField("Tipologia Utente", max_length=50, choices=ACCOUNT_TYPE_CHOICES, default='cliente')
    img_profilo = ProcessedImageField(upload_to='user_profile/', processors=[ResizeToCover(80,80)], format='PNG', options={'quality':60}, default='user_profile/profile_user.png')
    indirizzo = models.CharField("Indirizzo", max_length=250, blank=True, null=True)
    comune = models.CharField("Comune", max_length=150, blank=True, null=True)
    citta = models.CharField("Città", max_length=150, blank=True, null=True)
    cap = models.CharField("C.A.P.", max_length=5, blank=True, null=True ,validators=[RegexValidator(
        regex=r'^[0-9]{4,5}$',
        message="Puoi inserire solo 5 numeri",
    )])


    def __str__(self):
        return self.user.username
    
    #Per visualizzare immagine in Admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img_profilo.url}" width="150" />')
    
    #Salvo il CF in Maiuscolo nel DB
    def save(self, *args, **kwargs):
        if self.cf:
            self.cf = self.cf.upper()
            super(UserProfile, self).save(*args, **kwargs)
        return None

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

