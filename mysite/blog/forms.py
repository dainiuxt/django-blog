from django import forms
from .models import BlogPost, Comment

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_text']
        widgets = {
            'post_author': forms.HiddenInput(),
            'pub_time': DateTimeInput(), 
            }

class BlogPostUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_post': forms.HiddenInput(),
            'comment_author': forms.HiddenInput(),
            'pub_time': DateTimeInput(), 
            }

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
