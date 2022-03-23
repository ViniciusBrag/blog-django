from django.urls import path
from blogdjango.blog.views import blog

app_name = 'blog'
urlpatterns = [
    path('', blog, name='blog'),
]
