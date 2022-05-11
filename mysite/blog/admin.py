from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('post_author', 'post_title', 'pub_time')

class CommentAdmin(admin.ModelAdmin):
  list_display = ('comment_author', 'pub_time', 'comment_post')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
