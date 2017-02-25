from django.contrib import admin

# Register your models here.
from .models import Notebook,Note,Favorite

admin.site.register(Notebook)
admin.site.register(Note)
admin.site.register(Favorite)