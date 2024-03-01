from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    avatar = models.ImageField(upload_to='blog/avatar', default='/blog/avatar/default.png')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', default='/blog/default.jpg')
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def avatar_image(self):
        return format_html('<img src="{}" style="max-width:48px; max-height:48px"/>'.format(self.avatar.url))

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})
