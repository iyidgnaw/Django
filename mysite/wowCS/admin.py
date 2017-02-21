from django.contrib import admin

# Register your models here.
from .models import Notebook,Note

admin.site.register(Notebook)
admin.site.register(Note)