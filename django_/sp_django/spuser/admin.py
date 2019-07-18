from django.contrib import admin
from .models import Spuser
# Register your models here.

class SpuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

admin.site.register(Spuser, SpuserAdmin)

