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

  def __str__(self):
      return f'{self.post_title} by {self.post_author}'

  class Meta:
      verbose_name = 'Post'
      verbose_name_plural = 'Posts'


class Comment(models.Model):
  comment_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)
  comment_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  pub_time = models.DateTimeField('Publication time', null=True, blank=True)
  comment_text = models.TextField('Comment')

  def __str__(self):
      return f'{self.pub_time} by {self.comment_author}'

  class Meta:
      verbose_name = 'Comment'
      verbose_name_plural = 'Comments'

