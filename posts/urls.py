from django.conf.urls import url
from . import views

#   If multiple url.py files exist, app_name allows you specify in TEMPLATES which url file you want to use
app_name = 'posts'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
    # use regex to retrieve the id of the post/upvote
    # e.g. localhost:8000/posts/2/upvote
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    url(r'^created_by/(?P<author_id>[0-9]+)', views.created_by, name="created_by"),      #   Challenge answer version 1
    #url(r'^created_by/(?P<fk>[0-9]+)', views.created_by2, name="created_by")            #   Challenge answer version 2
]
