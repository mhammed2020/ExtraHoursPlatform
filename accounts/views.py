from django.shortcuts import render,redirect
from .models import Profile
from .forms import SignUpForm,ProfileForm,UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


#templates/user

def doctor_list(request) :
    doctors = Profile.objects.all()

    context = {'doctors' : doctors}
    return render(request,'user/doctor_list.html',context)

def doctor_detail(request,slug) :
    doctor_detail = Profile.objects.get(slug=slug)

    context = {'doctor_detail' : doctor_detail}
    return render(request,'user/doctor_detail.html',context)



# Create your views here.

def sign_up(request):
    if request.method == 'POST' : #save SignUpForm
        form = SignUpForm(request.POST)
        if  form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('/accounts/profile')

    else : #show  SignUpForm
        form = SignUpForm()
    context = {'form':form}
    return render(request,'registration/signup.html',context)



def profile(request):

    profile = Profile.objects.get(user = request.user)

    return render(request,'profile/profile.html',{'profile':profile})


def profile_edit(request):

    profile = Profile.objects.get(user = request.user)


    if request.method == 'POST':
        userform = UserForm(request.POST,instance =request.user)
        profileform = ProfileForm(request.POST,instance =profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()

            myform = profileform.save(commit = False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')

    else :
        userform = UserForm(instance = request.user)
        profileform = ProfileForm(instance = profile)

    return render(request,'profile/profile_edit.html',
    {'userform':userform,
    'profileform':profileform
    })

