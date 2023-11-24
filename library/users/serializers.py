from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.constants import DEFAULT_USERNAME
from users.mailing import test_task

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def create(self, validated_data):
        #FIXME! место для задачи в сельдерее
        username = validated_data.get(
            'username',
            DEFAULT_USERNAME,
        )
        user_email = validated_data.get(
            'email',
            settings.DEFAULT_EMAIL_RECIPIENT,
        )
        test_task.delay(username, user_email)
        return super().create(validated_data)
