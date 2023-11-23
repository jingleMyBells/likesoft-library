from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from users.serializers import UserCreateSerializer


User = get_user_model()


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
