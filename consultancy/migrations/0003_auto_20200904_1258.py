# Generated by Django 3.1 on 2020-09-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultancy', '0002_auto_20200829_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
