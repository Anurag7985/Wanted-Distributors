# Create your views here.
from django.shortcuts import render, redirect
from wd.models import TutorReg, StudentReg
from django.views.decorators.csrf import requires_csrf_token
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@requires_csrf_token
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user =fm.save()
            login(request, user)
            return redirect('home')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html',{'form':fm})

def login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                #print("Success")
                #login(request, user)    
                return HttpResponseRedirect('/dashboard')
    else:
        fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm})

        
        
    



def home(request):
    return render(request, 'home.html')



def dashboard(request):
    return render(request, 'dashboard.html')



def tutor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject_expert = request.POST.get('subjectExpert')
        biodata = request.POST.get('bio')
        submit_obj = TutorReg(name=name, email=email, subject_experties=subject_expert, bio=biodata)
        submit_obj.save()
  
    return render(request, 'tutor.html')



def student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjectRequired = request.POST.get('subject Required')
        contact = request.POST.get('contact')
        submit = StudentReg(name=name, email=email, subject_required=subjectRequired, contact_number=contact)
        submit.save()
  
    return render(request, 'student.html')