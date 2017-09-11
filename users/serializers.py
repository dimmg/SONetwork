from django.contrib.auth import get_user_model

from rest_framework import serializers

from .services import ClearBitService, HunterService


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'bio', 'email', 'first_name', 'gender', 'last_name', 'joined_at', 'password')

    def create(self, validated_data):
        account_details = ClearBitService.get_details_for_email(validated_data['email'])
        validated_data = {**account_details, **validated_data}

        user = get_user_model()(**validated_data)

        password = validated_data.get('password')
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            instance.save()

        return instance

    def validate_email(self, value):

        if not HunterService.is_valid_email(value):
            raise serializers.ValidationError('invalid, please use a valid one!')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('must contain at least 8 characters.')

        return value
