from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=255, null=False)
    father_name = models.CharField(max_length=255, null=False)
    birth_date = models.DateTimeField(auto_now=False, blank=True)
    birth_place = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.name, self.father_name)
