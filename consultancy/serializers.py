from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from jwtauth.serializers import UserCreateSerializer


class ProfileSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(partial=True )

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        owner = validated_data.pop('owner')
        user_data = UserCreateSerializer(owner).data
        user = User.objects.get(username=user_data['username'])
        profile = Profile.objects.create(owner=user, **validated_data)
        profile.save()
        return profile






