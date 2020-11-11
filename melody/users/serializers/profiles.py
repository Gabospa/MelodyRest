"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from melody.users.models import Profile


class ProfileModelSerialzier(serializers.ModelSerializer):
    """Profile model serialzier."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture',
            'birthdate',
            'country',
            'gender'
        )
