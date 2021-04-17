from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import users
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

@csrf_exempt
def register(request):
    if request.method == 'POST':
        print(request.POST)
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            if profile_form.cleaned_data['type'] == 'admin':
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.mobile = user_form.cleaned_data['mobile']
            profile_form.email = user_form.cleaned_data['mobile']
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile(request):
    user = Profile.objects.filter(user=request.user)[0]
    print(user.mobile)
    return render(request, 'users/profile.html', {'mobile': user.mobile, 'type': user.type})
