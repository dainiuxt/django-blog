from django.shortcuts import render, reverse, redirect
from blog.models import BlogPost, Comment, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogPostForm
from django.views.generic.edit import FormMixin

from django.views.generic import (
                                ListView,
                                DetailView,
                                DeleteView,
                                CreateView,
                                UpdateView,
                                )


def index(request):
    post_list = list(reversed(BlogPost.objects.all()))
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': posts})

class BlogPostView(DetailView):
  model = BlogPost
  template_name = 'blogpost.html'

class BlogPostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogpost = self.get_object()
        return self.request.user == blogpost.user

    def get_success_url(self):
        return reverse('blogpost', kwargs={'pk': self.object.id})

class BlogPostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogpost = self.get_object()
        return self.request.user == blogpost.user

    def get_success_url(self):
        return reverse('blogpost', kwargs={'pk': self.object.id})

# class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = BlogPost
#     template_name = 'my_blogpost_delete.html'

#     def get_success_url(self):
#         return reverse('index')

#     def test_func(self):
#         blogpost = self.get_object()
#         return self.request.user == blogpost.user


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} already exists!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Account with {email} already exist!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    return redirect('index')
        else:
            messages.error(request, 'Passwords didn\'t match!')
            return redirect('register')
    return render(request, 'registration/register.html')
