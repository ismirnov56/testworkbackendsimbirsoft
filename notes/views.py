from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from notes.models import NotesModel
from notes.permissions import IsAuthenticatedAndOwner
from notes.serializers import NotesSerializer


class NotesView(ModelViewSet):
    """
    View для работы с Записками
    Данная  view позваляет изменять, создавть, получать и удалять записки
    """
    # сериализатор
    serializer_class = NotesSerializer
    # организация доступа только владельцам записок и аутентифициорованным пользователям
    permission_classes = [IsAuthenticatedAndOwner]

    def get_queryset(self):
        """
        Делаем запросы в БД с помощью Django ORM
        Отдаем пользователю только те записки, которыми он владеет отсортированные по дате
        """
        return NotesModel.objects.filter(user=self.request.user.id).order_by('-date_create')

    def perform_create(self, serializer):
        """
        Присваиваем пользователю книги которые он создал
        """
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class NotesCountsView(APIView):
    """
    API View для получения количества записок
    Только для чтения
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Возвращаем количество записок исходя из пользователя, который прислал запрос
        """
        try:
            count = NotesModel.objects.filter(user=self.request.user).count()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data={'count': count}, status=status.HTTP_200_OK)
