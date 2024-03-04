from django.contrib.syndication.views import Feed
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Newest Posts"
    link = "/rss/feed"
    description = "Best Blog Ever."

    @staticmethod
    def items():
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
