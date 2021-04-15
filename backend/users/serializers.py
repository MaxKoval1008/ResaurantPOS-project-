from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, allow_blank=False, write_only=True)

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'], first_name=validated_data['first_name'],
            last_name=validated_data['last_name'], is_waiter=validated_data['is_waiter'],
            phone_number=validated_data['phone_number'], is_cooker=validated_data['is_cooker'],
            is_staff=validated_data['is_staff'], is_admin=validated_data['is_admin']
        )
        if validated_data['is_admin']:
            user.is_waiter = False
            user.is_cooker = False
            user.role = 1
        elif validated_data['is_waiter']:
            user.is_cooker = False
            user.role = 2
        elif validated_data['is_cooker']:
            user.role = 3
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number',
                  'is_admin', 'is_waiter', 'is_cooker', 'is_staff'
                  )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number',

                  )
