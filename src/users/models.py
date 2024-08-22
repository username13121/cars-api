from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = (
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        ordering = ('-id',)