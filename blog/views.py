from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    PostObjects = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())
    post = get_object_or_404(PostObjects, pk=pid)
    post.counted_views += 1
    post.save()
    content = {'post': post}
    return render(request, 'blog/blog-single.html', content)


def blog_category(request, category_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=category_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
