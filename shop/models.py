from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover, ResizeToFill
from django_cleanup import cleanup
from ckeditor.fields import RichTextField

class Category(models.Model):
    #Sub Category esempio Link:https://github.com/ShivamRohilllaa/django-categories-tree/blob/main/templates/index.html
    main_category = models.ForeignKey('self',null=True,blank=True, related_name='children_category', on_delete=models.CASCADE)
    name = models.CharField('Nome',max_length=200)
    slug = models.SlugField(max_length=200,unique=True, null=False, editable=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

        unique_together = ('slug', 'main_category',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    #Gestione delle sottocategorie
    def __str__(self):                           
        full_path = [self.name]                  
        k = self.main_category
        while k is not None:
            full_path.append(k.name)
            k = k.main_category
        return ' -> '.join(full_path[::-1])  

@cleanup.select
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', default='products/noimg.png')
    img_resize = ImageSpecField(source='image', processors=[ResizeToFill(800,800)], format='PNG', options={'quality':40})
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField("Quantità in magazzino", default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    #Per visualizzare immagine in Admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="150" />')
