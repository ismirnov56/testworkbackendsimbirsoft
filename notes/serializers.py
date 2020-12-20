from rest_framework import serializers

from .models import NotesModel


class NotesSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели записок
    Возврат полей: Id из бд, сама записка и дата сощдания
    """
    class Meta:
        model = NotesModel
        fields = ('id', 'note', 'date_create')
