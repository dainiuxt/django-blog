from django import forms
from .models import BlogPost, Comment
from django.contrib.auth.models import User

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_text']
        widgets = {
            'post_author': forms.HiddenInput(), 'pub_time': DateTimeInput(), 
            }
