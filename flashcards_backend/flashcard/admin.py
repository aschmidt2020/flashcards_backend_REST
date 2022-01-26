from django.contrib import admin

from .models import Collection, Flashcard

# Register your models here.
admin.site.register(Flashcard)
admin.site.register(Collection)