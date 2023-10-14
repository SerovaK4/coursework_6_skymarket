from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from ads.filter import AdFilter
from ads.models import Ad, Comment
from ads.permissions import ReadOrCreatePermission, OwnerOrAdminPermission
from ads.serializers import CommentSerializer

from ads.serializers import AdSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    serializer_class = AdSerializer
    pagination_class = AdPagination

    """
    настройка прав доступа
    """

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'me']:
            self.permission_classes = [ReadOrCreatePermission]
        else:
            self.permission_classes = [OwnerOrAdminPermission]
        return super(self.__class__, self).get_permissions()

    """
    ассоциациирует созданный объект с пользователем, который отправил запрос на его создание
    """

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    """
    фильтрует объекты Ads по автору и возвращает все ему принадлежащие объявления
    """

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    """
     добавления 'me' к стандартному набору методов
    """

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [OwnerOrAdminPermission]
        return super(self.__class__, self).get_permissions()

    """
    Возвращает список всех комментариев данного объявления
    """

    def get_queryset(self):

        ad = self.kwargs['ad_pk']
        return Comment.objects.filter(ad=ad).all()

    """
    ассоциациирует созданный объект с пользователем, который отправил запрос на его создание
    """

    def perform_create(self, serializer):
        ad = self.kwargs['ad_pk']
        serializer.save(author=self.request.user, ad_id=ad)
