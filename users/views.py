from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from .permissions import CustomUserPermissions
from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (CustomUserPermissions,)
