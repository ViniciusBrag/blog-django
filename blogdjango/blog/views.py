from django.shortcuts import render
from blogdjango.blog.forms import PostForm
from blogdjango.blog.models import Post, AboutBlog 
from django.views.generic import DetailView, ListView, CreateView

class PostList(ListView):
    queryset = Post.objects.filter(status_post=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutBlog(ListView):
    queryset = AboutBlog.objects.all()
    model = AboutBlog
    template_name = 'about_blog.html'
     
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'      