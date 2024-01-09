from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import PatientSignUpForm,DoctorSignUpForm
from .models import CustomUser

# Create your views here.

def home(request):
    return render(request, 'home.html')

def patient_signup(request):
    
    if request.method == "POST":
        form = PatientSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request,user,backend='app.backends.CustomUserBackend')
            return redirect('patient_dashboard')
        
    else:
        form = PatientSignUpForm()

    return render(request,'patient_signup.html', {'form': form})

def doctor_signup(request):
    
    if request.method == "POST":
        form = DoctorSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request,user,backend='app.backends.CustomUserBackend')
            return redirect('doctor_dashboard')
        
    else:
        form = PatientSignUpForm()

    return render(request,'doctor_signup.html', {'form': form})


def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('patient_dashboard')
        else:
            return render(request, 'patient_login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'patient_login.html')

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_exists = CustomUser.objects.filter(username=username).exists()
        print(user_exists)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            
            return redirect('doctor_dashboard')
        else:
            return render(request, 'doctor_login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'doctor_login.html')

def patient_dashboard(request):
    user = request.user
    return render(request, 'patient_dashboard.html', {'user': user})

def doctor_dashboard(request):
    user = request.user
    return render(request, 'doctor_dashboard.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('home') 


