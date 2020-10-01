from rest_framework import serializers
from .models import Profile, Question
from django.contrib.auth.models import User
from jwtauth.serializers import UserCreateSerializer


class ProfileSerializer(serializers.ModelSerializer):
    owner = UserCreateSerializer(partial=True)
    birth_date = serializers.DateTimeField(format="%d/%m/%Y %I:%M %p", input_formats="%d/%m/%Y %I:%M %p")

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
    owner = UserCreateSerializer(partial=True)
    profile = ProfileSerializer(partial=True)
    profile2 = ProfileSerializer(partial=True, required=False)
    fees = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)

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




