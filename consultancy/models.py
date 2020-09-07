from django.db import models
from django.contrib.auth.models import User
from .utils import QuestionTypes, Gender

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=255, null=False)
    father_name = models.CharField(max_length=255, null=False)
    birth_date = models.DateTimeField(null=False, auto_now_add=True)
    birth_place = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    gender = models.IntegerField(choices=Gender.choices(), default=Gender.MALE)
    main = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.name, self.father_name)


class Question(models.Model):
    question_text = models.TextField()
    type = models.CharField(max_length=20)
    type = models.IntegerField(choices=QuestionTypes.choices(), default=QuestionTypes.HOROSCOPE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile2')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
