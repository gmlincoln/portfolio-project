from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Custom_User(AbstractUser):
    
    USER = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]

    user_type = models.CharField(choices=USER, max_length=100, null=True)
    
    def __str__(self):
        
        return f"{self.username}-{self.first_name} {self.last_name}"

class Resume_Model(models.Model):

    user = models.OneToOneField(Custom_User, null=True, on_delete=models.CASCADE)

    GENDER = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    profile_pic = models.ImageField(null=True)
    designation = models.CharField(max_length=100, null=True)
    career_summary = models.TextField(max_length=400, null=True)
    address = models.CharField(max_length=200, null=True)
    contact_no = models.CharField(max_length=30, null=True)
    linkedin_url = models.URLField(max_length=100, null=True)
    gender  = models.CharField(choices=GENDER, max_length=40, null=True)

    def __str__(self):

        return f"{self.user.username}--{self.designation}"
