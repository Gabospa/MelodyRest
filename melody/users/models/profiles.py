"""Profile model."""


# Django
from django.db import models

# Utilities
import pytz
from melody.utils.models import MelodyModel


class Profile(MelodyModel):
    """ Profile model.

    A profile holds user's public data, like picture and public playlists.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    birthdate = models.DateTimeField()

    country = models.CharField(
        max_length=2,
        choices=(pytz.country_names.items(), (None, ' '))
    )

    GENDER_CHOICES = [
        ('ML', 'Male'),
        ('FM', 'Female'),
        ('NB', 'Not Binary')
    ]

    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES)
     
    def __str__(self):
        """ Return user's str representation."""
        return str(self.user)
        