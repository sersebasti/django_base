from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ['title','username']
    #list_editable = ['title']
    list_per_page = 10
    #list_filter = ['title']
    search_fields =  ['title']
    #autocomplete_fields = ['tipo_prodotto']