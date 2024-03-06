from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth import mixins  as auth_mixins
from blog_system.blogs.models import Blog
from blog_system.common.utils import can_user_create_blog


# Create your views here.
class BlogsListView(views.ListView):
    template_name = 'blogs/list.html'
    model = Blog

class BlogDetailView(views.DetailView):
    template_name = 'blogs/detail.html'
    model = Blog


class BlogsCreateView(auth_mixins.LoginRequiredMixin,views.CreateView):
    template_name = 'blogs/create.html'
    model = Blog
    fields = ('name', 'description')
    def dispatch(self, request, *args, **kwargs):
        if not can_user_create_blog(request.user):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class BlogUpdateView():
    pass
class BlogDeleteView():
    pass