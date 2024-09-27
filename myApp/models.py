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

    profile_pic = models.ImageField(upload_to='Media/Profile_Pic', null=True)
    designation = models.CharField(max_length=100, null=True)
    career_summary = models.TextField(max_length=400, null=True)
    address = models.CharField(max_length=200, null=True)
    contact_no = models.CharField(max_length=30, null=True)
    linkedin_url = models.URLField(max_length=100, null=True)
    gender  = models.CharField(choices=GENDER, max_length=40, null=True)

    def __str__(self):

        return f"{self.user.username}--{self.designation}"




class Education_Model(models.Model):

    user = models.ForeignKey(Custom_User, null=True, on_delete=models.CASCADE)

    STUDY_LEVEL = [
        ('ssc', 'SSC'),
        ('hsc', 'HSC'),
        ('bsc', 'BSc'),
        ('msc', 'MSc'),
        ('others', 'Others'),
    ]
    study_level = models.CharField(choices=STUDY_LEVEL, max_length=20, null=True)
    educational_institute = models.CharField(max_length=200, null=True)
    passing_year = models.CharField(max_length=10, null=True) 

    class Meta:
        unique_together = ('user', 'study_level')

    def __str__(self):
        return f"{self.user.username}--{self.study_level}--{self.passing_year}"

class LanguageName(models.Model):

    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"


class Language_Model(models.Model):

    PROFICIENCY_LEVEL = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('fluent', 'Fluent'),
        ('native', 'Native'),
    ]

    user = models.ForeignKey(Custom_User, null=True, on_delete=models.CASCADE)

    language_name = models.ForeignKey(LanguageName, null=True, on_delete=models.CASCADE)

    proficiency = models.CharField(choices=PROFICIENCY_LEVEL, max_length=100, null=True)


    def __str__(self):

        return f"{self.user.username}--{self.language_name}--{self.proficiency}"
    
class SkillName(models.Model):

    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Skill_Proficiency(models.Model):

    PROFICIENCY = [
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced'),
        ('expert','Expert'),
    ]

    proficiency_level = models.CharField(choices=PROFICIENCY, null=True, max_length=100)

    def __str__(self):

        return f"{self.proficiency_level}"
    

class Skill_Model(models.Model):

    user = models.ForeignKey(Custom_User, max_length=100, null=True, on_delete=models.CASCADE)
    skill_name = models.ForeignKey(SkillName, null=True, on_delete=models.CASCADE)
    proficiency = models.ForeignKey(Skill_Proficiency, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'skill_name')

    def __str__(self):
        return f"{self.user.username}--{self.skill_name}--{self.proficiency}"
    

    