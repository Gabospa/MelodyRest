"""Users serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from melody.users.models import User


class UserModelSerialzier(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )
