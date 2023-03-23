from django.db import models
from django.contrib.auth.forms import UserCreationForm

class TutorReg(models.Model):
    name = models.CharField(max_length=255, default='default name')
    email = models.EmailField(max_length=255, default='default email')
    subject_experties = models.CharField(max_length=100, default='default subject')
    bio = models.TextField(default='')

class StudentReg(models.Model):
    name = models.CharField(max_length=100, default='default name')
    email = models.EmailField(default='default email')
    subject_required = models.CharField(max_length=100, default='default subject')
    contact_number = models.CharField(max_length=13, default='0000000000')
    
    


