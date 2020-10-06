from rest_framework import serializers
from .models import Profile, Question, Answer
from django.contrib.auth.models import User
from jwtauth.serializers import UserCreateSerializer
from .utils import QuestionTypes


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    owner = UserCreateSerializer(partial=True)
    birth_date = serializers.DateTimeField(format="%d/%m/%Y %I:%M %p", input_formats=None)

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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.middle_name = validated_data.get('middle_name',instance.middle_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.birth_place = validated_data.get('birth_place', instance.district)
        instance.district = validated_data.get('district', instance.district)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.main = validated_data.get('main', instance.main)
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer(partial=True)

    class Meta:
        model = Answer
        fields = '__all__'
        depth = 0


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    owner = UserCreateSerializer(partial=True)
    profile = ProfileSerializer(partial=True)
    profile2 = ProfileSerializer(partial=True, required=False)
    fees = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        owner = User.objects.get(pk=validated_data.pop('owner').get('id'))
        profile = Profile.objects.get(pk=validated_data.pop('profile').get('id'))

        profile2 = None
        if validated_data['type'] is int(QuestionTypes.MATCHMAKING):
            profile2 = Profile.objects.get(pk=validated_data.pop('profile2').get('id'))

        question = Question.objects.create(owner=owner, profile=profile, profile2=profile2, **validated_data)
        return question





