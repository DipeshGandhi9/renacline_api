from rest_framework import serializers
from .models import Profile, Question
from django.contrib.auth.models import User
from jwtauth.serializers import UserCreateSerializer


class ProfileSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(partial=True)
    birth_date = serializers.DateTimeField(format="%d/%m/%Y %I:%M %p")

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


class QuestionSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(partial=True )

    class Meta:
        model = Question
        fields = '__all__'

    # def create(self, validated_data):
    #     owner = validated_data.pop('owner')
    #     user_data = UserCreateSerializer(owner).data
    #     user = User.objects.get(username=user_data['username'])
    #     profile = Profile.objects.create(owner=user, pro **validated_data)
    #     profile.save()
    #     return profile




