from django.db import models


class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)
    class Meta():
        db_table="User"
