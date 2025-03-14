from django.contrib.sitemaps import Sitemap
from .models import Product, Review


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    # priority = 0.5

    def items(self):
        return Product.objects.filter()

    def lastmod(self, obj: Product):
        return obj.modified
