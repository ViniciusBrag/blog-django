from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('/about_blog/', views.AboutBlog.as_view(), name='about_blog'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
]
