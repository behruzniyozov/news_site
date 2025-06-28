from rest_framework import serializers
from accounts.models import User

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'bio',
            'profile_image'
        ]
        read_only_fields = ['is_active', 'is_staff', 'is_superuser']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.bio = validated_data.get('bio', instance.bio)
        if 'profile_image' in validated_data:
            instance.profile_image = validated_data['profile_image']
        
        instance.save()
        return instance