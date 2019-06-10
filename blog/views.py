from django.views.generic import ListView, DetailView
from blog.models import *
from django.shortcuts import render





def blog(request):
    return render(request, 'blog/blog_base.html', locals())






# class BlogListView(ListView):
#     model = Post
#     template_name = 'home.html'
#
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'



