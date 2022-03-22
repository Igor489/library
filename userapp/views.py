from rest_framework import mixins, viewsets
from .serializers import UserSerializer, UserSerializerUserData
from .models import User


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        print('version', self.request.version)
        if self.request.version == '0.2':
            return UserSerializerUserData
        return UserSerializer
