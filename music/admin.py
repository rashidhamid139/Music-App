from django.contrib import admin
from . models import Album, Song
# Register your models here.
admin.site.register(Song)
admin.site.register(Album)