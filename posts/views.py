# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.pub_date = timezone.datetime.now()
            #   RETRIEVE THE CURRENTLY LOGGED IN USER
            post.author = request.user
            post.save()
            #   IF SUCCESSFUL POST, REDIRECT BACK TO THE HOMEPAGE
            return redirect('home')
        else:
            args = {'error': 'ERROR: You must include a Title and URL to create a post'}
            return render(request, 'posts/create.html', args)
    else:
        return render(request, 'posts/create.html')


#   RETURN LIST OF ALL POSTS
def home(request):
    #   retrieve all Posts objects
    posts = Post.objects.order_by('-votes_total')
    args = {'posts':posts}
    return render(request, 'posts/home.html', args)


def created_by(request, author_id):
    user = User.objects.get(pk=author_id)
    posts = Post.objects.filter(author=user)
    return render(request, 'posts/created_by.html', {'posts': posts})


def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home')


def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('home')



