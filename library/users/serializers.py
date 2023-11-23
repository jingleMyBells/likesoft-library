from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def create(self, validated_data):
        #FIXME! место для задачи в сельдерее
        return super().create(validated_data)
