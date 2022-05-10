from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('<int:pk>', views.BlogPostView.as_view(), name='blogpost'),
    path('new/', views.BlogPostCreateView.as_view(), name='blogpost-new'),
]
