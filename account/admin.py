from django.contrib import admin
from .models import Carousel, CarouselCat, UserProfile
#Per Utente
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#Carousel Admin area
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'sottotitolo', 'img_preview','pubblicato', 'categoria']
    search_fields = ['titolo', 'sottotitolo', 'corpo']
    list_filter = ['pubblicato','categoria','titolo', 'sottotitolo']
    list_editable = ['pubblicato']
    readonly_fields = ['img_preview']

admin.site.register(CarouselCat)

#Metodi Utenti
#Link: https://github.com/veryacademy/Django-4.x-ORM-Course/tree/main/customer-user-model-add-user-fields
class CustomUserAdmin(admin.StackedInline):
    model = UserProfile
    can_delete = False
    readonly_fields = ['img_preview']
    
class AccountsUserAdmin(UserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines =[]
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines =[CustomUserAdmin]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)

# class AccountsUserAdmin(admin.ModelAdmin):
#     inlines = [CustomUserAdmin]
    
admin.site.unregister(User)
admin.site.register(User,AccountsUserAdmin)