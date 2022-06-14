from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from profiles.models import Profile

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Is Already In Use')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()

                # Log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # Create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,
                                                     id_user=user_model.id,
                                                     firstname=firstname,
                                                     lastname=lastname)
                new_profile.save()
                return redirect('profile/settings')
    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
            
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')