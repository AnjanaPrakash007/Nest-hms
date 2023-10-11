from django.contrib.auth.models import User
from django.db import models

# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     is_admin = models.BooleanField(default=False)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('student', 'Student')])
    # Add other user-specific fields here

    def __str__(self):
        return self.user.username
    
class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=10, unique=True)
    # Add other student-specific fields here
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    religion = models.CharField(max_length=30)
    caste = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    def __str__(self):
        return self.user_profile.user.username
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.date}"
