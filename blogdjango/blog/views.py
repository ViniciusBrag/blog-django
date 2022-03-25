from django.shortcuts import render
from blogdjango.blog.models import Post
from django.views.generic import DetailView, ListView

class PostList(ListView):
    queryset = Post.objects.filter(status_post=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'