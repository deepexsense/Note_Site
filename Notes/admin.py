from django.contrib import admin

# Register your models here.
from Notes.models import Note, Category

admin.site.register(Note)
admin.site.register(Category)
