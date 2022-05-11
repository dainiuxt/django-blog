from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('<int:pk>', views.BlogPostView.as_view(), name='blogpost'),
    path('new/', views.BlogPostCreateView.as_view(), name='blogpost-new'),
    path('<int:pk>/delete/', views.BlogPostDeleteView.as_view(), name='blogpost-delete'),
    path('<int:pk>/edit/', views.BlogPostUpdateView.as_view(), name='blogpost-edit'),
    path('<blogpost>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('<blogpost>/comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
]
