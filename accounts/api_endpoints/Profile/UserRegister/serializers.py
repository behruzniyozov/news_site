from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from accounts.models import User

from accounts.api_endpoints.Profile.UserRegister.tokens import (
    generate_user_register_token,
    verify_user_register_token
)

User = get_user_model()


class UserRegisterRequestSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'token']
        read_only_fields = ['id', 'token']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_active=False  # optional: if you require email confirmation
        )
        user.set_password(validated_data['password'])
        user.save()
        
        # Attach token to instance so it appears in the output
        user.token = generate_user_register_token(user)
        return user


class UserRegisterVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, value):
        user_id = verify_user_register_token(value)
        if not user_id:
            raise serializers.ValidationError("Invalid or expired token.")
        try:
            self.user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")
        return value

    def save(self):
        # Optional: activate user
        self.user.is_active = True
        self.user.save()
        return self.user