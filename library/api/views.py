from djoser.views import UserViewSet

from users.models import User
from .serializers import UserSerializer


class UserViewSet(UserViewSet):
    queruet = User.objects.all()
    serializer_class = UserSerializer
