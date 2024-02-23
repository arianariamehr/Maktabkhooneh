from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())
    if kwargs.get('category_name') is not None:
        posts = posts.filter(category__name=kwargs['category_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    PostObjects = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())
    post = get_object_or_404(PostObjects, pk=pid)
    post.counted_views += 1
    post.save()
    content = {'post': post}
    return render(request, 'blog/blog-single.html', content)
