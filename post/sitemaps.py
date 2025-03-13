from django.contrib.sitemaps import Sitemap
from post.models import BlogPost


class PostSitemap(Sitemap):
    changefreq = "weekly"
    # priority = 0.5

    def items(self):
        return BlogPost.objects.filter(is_visible=True)

    def lastmod(self, obj: BlogPost):
        return obj.updated_at