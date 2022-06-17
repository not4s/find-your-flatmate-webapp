from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# def profile_page(request):
#     return HttpResponse('<h1>Profile Page Placeholder<h1>')

# @login_required(login_url='signin')
# def settings(request):

#     user_profile = Profile.objects.get(user=request.user)

#     if request.method == 'POST':

#         if request.FILES.get == None:
#             image = user_profile.profile_img
#         else:
#             image = request.FILES.get('image')

#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         email = request.POST['email']
#         about = request.POST['about']
#         location = request.POST['location']
#         studies_at = request.POST['studies_at']

#         user_profile.image = image
#         user_profile.firstname = firstname
#         user_profile.lastname = lastname
#         user_profile.email = email
#         user_profile.about = about
#         user_profile.location = location
#         user_profile.studies_at = studies_at
#         user_profile.save()
        
#         return redirect('settings')

#     return render(request, 'setting.html', {'user_profile': user_profile})
