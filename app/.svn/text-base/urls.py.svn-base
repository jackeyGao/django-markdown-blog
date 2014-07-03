from django.conf.urls import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.sitemaps import sitemaps
from blog.views import *
from app.settings import is_sae, MEDIA_ROOT


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='main'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^tags/$', tag, name='tags'),
    url(r'^search/$', search, name='search'),
    url(r'^blogList/', home),
    url(r'^tagSearchList/(.*)/$', tagSearchList),
    url(r'^download/(.*)/$', download),
    url(r'^page/(.*)/$', page),
    url(r'^500/', error500),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nAllow: /", mimetype="text/plain")),
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

#filebrowser
if not is_sae:
    from filebrowser.sites import site
    
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}),
        url(r'^admin/filebrowser/', include(site.urls)),
)
