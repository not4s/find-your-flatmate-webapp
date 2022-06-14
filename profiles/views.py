from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from profiles.models import Profile

def profile_page(request):
    return HttpResponse('<h1>Profile Page Placeholder<h1>')

@login_required(login_url='signin')
def settings(request):

    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.FILES.get == None:
            image = user_profile.profile_img
        else:
            image = request.FILES.get('image')

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        about = request.POST['about']
        location = request.POST['location']
        studies_at = request.POST['studies_at']

        user_profile.image = image
        user_profile.firstname = firstname
        user_profile.lastname = lastname
        user_profile.email = email
        user_profile.about = about
        user_profile.location = location
        user_profile.studies_at = studies_at
        user_profile.save()
        
        return redirect('settings')

    return render(request, 'setting.html', {'user_profile': user_profile})
