from ast import mod
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from tinymce.models import HTMLField

class BlogPost(models.Model):
  post_title = models.CharField('Post tile', max_length=500, null=True)
  post_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  pub_time = models.DateTimeField('Publication time', null=True, blank=True)
  post_text = HTMLField()

class Comment(models.Model):
  comment_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  pub_time = models.DateTimeField('Publication time', null=True, blank=True)
  comment_text = models.TextField('Comment')
