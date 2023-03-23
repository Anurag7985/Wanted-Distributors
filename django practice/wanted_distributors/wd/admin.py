from django.contrib import admin
from .models import TutorReg
from .models import StudentReg

# Register your models here.
admin.site.register(TutorReg)
admin.site.register(StudentReg)