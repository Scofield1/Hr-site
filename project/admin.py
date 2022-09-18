from django.contrib import admin
from .models import *
# Register your models here.

class Registered_mailAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_per_page = 10
    search_fields = ['email']

admin.site.register(Registered_mail, Registered_mailAdmin)