from django.contrib import admin
from blogdjango.blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status_post', 'created_on')
    list_filter = ("status_post",)
    search_fields = ['title', 'content',]
    prepopulated_fields = {'slug': ('title',)}





