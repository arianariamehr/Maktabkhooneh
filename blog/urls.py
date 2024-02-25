from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('category/<str:category_name>', blog_view, name='category'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('<int:pid>', blog_single, name='single'),
    path('search/', blog_search, name='search')
]
