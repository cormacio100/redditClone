# -*- coding: utf-8 -*-
# DOCUMENTATION @ https://docs.djangoproject.com/en/1.11/topics/auth/default/
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already in use'})
            except User.DoesNotExist:
                #   CREATE USER ACCOUNT
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                #   LOG THE NEW USER IN
                login(request, user)
                print('the POST worked')
                return render(request, 'accounts/signup.html')
        else:
            args = {'error': 'Passwords did not match'}
            return render(request, 'accounts/signup.html', args)
    else:
        return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)

            #   CHECK IF USER HAS BEEN FORCED TO LOGIN WHILE TRYING TO ACCESS A RESTRICtED PTGE.
            #   IF SO, FORWARD THE USER TO WHERE THE VARIABLE 'NEXT' IS POINTING
            if 'next' in request.POST:
                if request.POST['next'] is not None:    # NOT NECESSARY
                    return redirect(request.POST['next'])
            args = {'error': 'Logged in successfully'}
            return render(request, 'accounts/login.html', args)
        else:
            args = {'error': 'User not found'}
            return render(request, 'accounts/login.html', args)
    else:
        return render(request, 'accounts/login.html')


@login_required()
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        #args = {'error': 'Logged out successfully'}
    else:
        #args = {'error': 'Logged out failed'}
        print('log out failed')
    return redirect('home')

