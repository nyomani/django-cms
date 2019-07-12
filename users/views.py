from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import (
    ProfileUpdateForm,
    VoterRegistrationForm
)
from voters.models import PersonRegistration

def register(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in as {username}')
            return redirect('voter-registration')
    else:
        form = ProfileUpdateForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def update_profile(request):
    print('update-profile',request)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('voter-registration')
        else:
            print('Form is not valid')
    else:
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
        'form': p_form
    }

    return render(request, 'users/update-profile.html', context)

@login_required
def voter_registration(request):
    if request.method == 'POST':
        voting_method=request.POST.get('votingMethod')
        person=request.user
        voter = Group.objects.get(name='Voter')
        person.grops.add(voter)
        reg = PersonRegistration(person=person,votingMethod=voting_method)
        v_form = VoterRegistrationForm(request.POST,
                                   instance=reg)
        if  v_form.is_valid():
            v_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            print('Form is not valid')
    else:
        v_form = VoterRegistrationForm()

    context = {
        'form': v_form
    }

    return render(request, 'users/voter-registration.html', context)

# Create your views here.# Create your views her# Create your views here.# Create your views here.# Create your views here.e.