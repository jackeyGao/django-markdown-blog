from django.contrib.sitemaps import GenericSitemap
from django.core.urlresolvers import reverse
from django.contrib import sitemaps
from blog.models import Blog

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['archive', 'tags']

    def location(self, item):
        return reverse(item)


blogs_dict = {
    'queryset': Blog.objects.filter(is_valid=1),
    'date_field': 'updated',
}

sitemaps = {
    'blogs': GenericSitemap(blogs_dict, priority=0.6, changefreq='daily'),
    'static': StaticViewSitemap,
}
