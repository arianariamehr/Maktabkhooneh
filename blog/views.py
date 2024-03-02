from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())
    if kwargs.get('category_name') is not None:
        posts = posts.filter(category__name=kwargs['category_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 4)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    post.counted_views += 1
    post.save()
    content = {'post': post}
    return render(request, 'blog/blog-single.html', content)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if search := request.GET.get('s'):
            posts = posts.filter(content__contains=search)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
