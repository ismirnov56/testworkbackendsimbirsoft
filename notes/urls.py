from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

"""
создаем url для пользования API
"""
router = SimpleRouter()
router.register(r'notes', NotesView, basename='Notes')

urlpatterns = [
    path('notescount/', NotesCountsView.as_view()),
]

urlpatterns += router.urls
