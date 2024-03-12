from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment successfully submitted.')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment could not be submitted.')

    posts = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(post=post.id, approved=True)
    post.counted_views += 1
    post.save()

    if not post.login_require:
        form = CommentForm()
        content = {'post': post, 'comments': comments, 'form': form}
        return render(request, 'blog/blog-single.html', content)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))



def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if search := request.GET.get('s'):
            posts = posts.filter(content__contains=search)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
