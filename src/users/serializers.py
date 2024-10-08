from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'is_staff')
