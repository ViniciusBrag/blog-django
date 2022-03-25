from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

class Post(models.Model):
    """
    Class Post for insert information about post in database.
    Args:
        models (_type_): _description_
        models a modeling de information for connect a database

    Returns:
        _type_: _description_
        Ordering: order based a last post
        

    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    updated_on = models.DateTimeField(auto_now = True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status_post = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content = self.content.upper()
        super().save(*args, **kwargs)    

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})