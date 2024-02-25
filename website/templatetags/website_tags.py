from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag('website/home-recent-posts.html')
def active_recent_blog_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}
