from django.conf.urls import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.sitemaps import sitemaps
from blog.views import *
from app.settings import is_sae


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexListView.as_view(), name='index'),
    url(r'^page/(?P<slug>.*)/$', BlogDetailView.as_view(), name='detail'),
    url(r'^archive/$', ArchiveListView.as_view(), name='archive'),
    url(r'^tags/$', TagsPageListView.as_view(), name='tags'),
    url(r'^tagSearchList/(?P<tag>[\w|\.|\-]+)/$',  TagsListView.as_view(), name='taglist'),
    url(r'^download/(.*)/$', download),
    url(r'^500/', error500),
    url(r'^robots\.txt', lambda r: HttpResponse("User-agent: Baiduspider\nDisallow: /\n\nUser-agent: baiduspider\nDisallow: /", mimetype="text/plain")),
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
