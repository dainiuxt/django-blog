from django.shortcuts import render, reverse, redirect, get_object_or_404
from blog.models import BlogPost, Comment, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogPostForm, BlogPostUpdateForm, CommentForm, CommentUpdateForm
from django.views.generic.edit import FormMixin

from django.views.generic import (
                                DetailView,
                                DeleteView,
                                CreateView,
                                UpdateView,
                                )


def index(request):
    post_list = list(reversed(BlogPost.objects.all()))
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = self.kwargs["pk"]

    form = CommentForm()
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comment_set.all()

    context['post'] = post
    context['comments'] = comments
    context['form'] = form
    return context

  def post(self, request, *args, **kwargs):
    form = CommentForm(request.POST)
    self.object = self.get_object()
    context = super().get_context_data(**kwargs)

    post = BlogPost.objects.filter(id=self.kwargs['pk'])[0]
    comments = post.comment_set.all()

    context['post'] = post
    context['comments'] = comments
    context['form'] = form

    if form.is_valid():
        comment_author = self.request.user
        comment_text = form.cleaned_data['comment_text']
        comment = Comment.objects.create(comment_text=comment_text, comment_author=comment_author, comment_post=post)

        form = CommentForm()
        context['form'] = form
        return self.render_to_response(context=context)

    return self.render_to_response(context=context)


class BlogPostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_update.html'

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogpost = self.get_object()
        return self.request.user == blogpost.post_author

    def get_success_url(self):
        return reverse('blogpost', kwargs={'pk': self.object.id})


class BlogPostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = BlogPost
    form_class = BlogPostUpdateForm
    template_name = 'blogpost_update.html'

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        blogpost = self.get_object()
        return self.request.user == blogpost.post_author

    def get_success_url(self):
        # blogpost = self.get_object()
        return reverse('blogpost', kwargs={'pk': self.object.id})

class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blogpost_delete.html'

    def get_success_url(self):
        return reverse('index')

    def test_func(self):
        blogpost = self.get_object()
        return self.request.user == blogpost.post_author


class CommentCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'blogpost.html'

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.comment_author

    def get_success_url(self):
        return reverse('comment', kwargs={'pk': self.object.id})

class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    form_class = CommentUpdateForm
    template_name = 'comment_edit.html'

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.comment_author

    def get_success_url(self):
        comment = self.get_object()
        return reverse('blogpost', kwargs={'pk': comment.comment_post.id})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse('blogpost', kwargs={'pk': self.object.id})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.comment_author


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
