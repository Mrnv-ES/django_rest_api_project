from rest_framework import mixins, viewsets
from usersapp.models import User
from usersapp.serializers import UserModelSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
