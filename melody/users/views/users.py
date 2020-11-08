"""Users views."""

# Django REST Framework
from rest_framework import viewsets

# Serializers
from melody.users.serializers import UserModelSerialzier

# Models
from melody.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """User view set."""

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerialzier
    lookup_field = 'username'
