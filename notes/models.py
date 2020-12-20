from django.conf import settings
from django.db import models
from django.utils import timezone


class NotesModel(models.Model):
    """
    Модель Записки
    """
    # поле записки Текстовое не пустое
    note = models.TextField(blank=False)
    # внешний ключ пользователь, при удалении пользователя удаляется все записки
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner'
    )
    """
    дата создания устанавливаем значение времени создания, чтобы не задумываться о передачи времени во время создания
    Время серверное, на фронте происходит преобразование во время браузерное
    """
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        Опредяем вывод, которым будет пользоваться django admin
        """
        return f'Note id: {self.id} owner email: {self.user.email}'
