from django.contrib import admin
from .models import Category, Product
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','main_category','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','quantity','category','available','created', 'updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','quantity','available'] #Per rendere editabili i campi ditettamente dalla lista
    search_fields = ['name','description']
    readonly_fields = ['img_preview']
    prepopulated_fields = {'slug': ('name',)}