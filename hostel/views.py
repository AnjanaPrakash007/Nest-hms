# views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from .models import CustomUser
from .forms import StudentRegistrationForm

def admin_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            return redirect('admin_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'admin_registration.html', {'form': form})

# views.py

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('student_dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})
