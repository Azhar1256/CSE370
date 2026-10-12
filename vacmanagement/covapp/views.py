from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from .forms import VaccineRegistrationForm

from .models import VaccineRegistration
from .models import Notices

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def userprofile(request):
    data = VaccineRegistration.objects.all()
    news = Notices.objects.all()
    
    context = {
        'data': data,
        'news': news,
    }
    
    return render(request, 'covapp/user-profile.html', context)

@login_required
def vacregistration(request):
    form = VaccineRegistrationForm()
    
    if request.method == 'POST':
        form = VaccineRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userProfile')
            
    
    context = {
        'form': form,
    }
    
    return render(request, 'covapp/vac-reg.html', context)

@login_required
def certificatepage(request, pk):
    user_data = get_object_or_404(VaccineRegistration, id=pk)
    
    context = {
        'user_data': user_data,
    }
    
    return render(request, 'covapp/certificate.html', context)

@login_required
def editdetails(request, pk):
    vaccineRegistration = get_object_or_404(VaccineRegistration, id=pk)
    form = VaccineRegistrationForm(instance = vaccineRegistration)
    
    if request.method == 'POST':
        form = VaccineRegistrationForm(request.POST, instance = vaccineRegistration)
        if form.is_valid():
            form.save()
            return redirect('userProfile')
        
    context = {
        'form': form
    }
    
    return render(request, 'covapp/edit-details.html', context)



@login_required
def delete_details(request, pk):
    
    data = get_object_or_404(VaccineRegistration, id=pk)
    
    if request.method == 'POST':
        data.delete()
        return redirect('userProfile')
    
    context = {
        'data': data
    }
    
    return render(request, 'covapp/delete-details.html', context)

def login_page(request):
    if request.method == 'POST':
        u = request.POST.get('u')
        p = request.POST.get('p')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('userProfile')
        
    return render(request, 'covapp/login.html')

def register_page(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    
    context = {
        'form': form
    }
    return render(request, 'covapp/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('loginPage')