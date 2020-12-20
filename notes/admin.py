from django.contrib import admin
from .models import NotesModel

# регистрация модели для django admin
admin.site.register(NotesModel)
