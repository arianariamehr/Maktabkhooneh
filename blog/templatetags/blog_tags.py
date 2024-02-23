from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag('blog/blog-popular-posts.html')
def blog_popular_posts(arg=4):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def blog_post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    categories_dict = {}
    for category in categories:
        post_count = posts.filter(category=category).count()
        categories_dict[category.name] = post_count
    return {'categories': categories_dict}
