from rest_framework import mixins, viewsets
from usersapp.models import User
from usersapp.serializers import UserModelSerializer, UserModelSerializerFullVersion


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    # serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerFullVersion
        return UserModelSerializer
