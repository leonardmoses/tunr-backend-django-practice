#default import
from django.contrib import admin
#our own import
from .models import Artist

# Register your models here.
admin.site.register(Artist)