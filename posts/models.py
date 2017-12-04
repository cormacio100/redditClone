# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    #   Link to USER OBJECT in the database
    author = models.ForeignKey(User)
    votes_total = models.IntegerField(default=1)
    thumbs_up = models.IntegerField(default=1)
    thumbs_down = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')