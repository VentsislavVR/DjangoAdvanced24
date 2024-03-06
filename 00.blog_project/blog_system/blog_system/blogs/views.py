from django.shortcuts import render
from django.views import generic as views

from blog_system.blogs.models import Blog


# Create your views here.
class BlogsListView(views.ListView):
    template_name = 'blogs/list.html'
    model = Blog

class BlogDetailView(views.DetailView):
    template_name = 'blogs/detail.html'
    model = Blog


class BlogsCreateView(views.CreateView):
    template_name = 'blogs/create.html'
    model = Blog
    fields = ('name', 'description')


class BlogUpdateView():
    pass
class BlogDeleteView():
    pass