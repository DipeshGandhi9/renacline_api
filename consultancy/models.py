from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .utils import QuestionTypes, Gender

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=255, null=False)
    middle_name = models.CharField(max_length=255, null=False)
    birth_date = models.DateTimeField(null=False, auto_now_add=True)
    birth_place = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    gender = models.IntegerField(choices=Gender.choices(), default=Gender.MALE)
    main = models.BooleanField(default=False)
    phone = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.name, self.father_name)


class Question(models.Model):
    question_text = models.TextField()
    type = models.IntegerField(choices=QuestionTypes.choices(), default=QuestionTypes.HOROSCOPE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile2')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
