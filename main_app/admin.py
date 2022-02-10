from django.contrib import admin

# Register your models here.

from .models import Artist, Song # import the Artist model from models.py
# Register your models here.

admin.site.register(Artist) # this line will add the model to the admin panel
admin.site.register(Song) # this line will add the model to the admin panel
