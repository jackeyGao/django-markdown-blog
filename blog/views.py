# -*- coding:utf-8 -*-
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response,get_object_or_404 
from blog.models import Blog, Tag

from django.views.generic import ListView, DetailView

from django.db.models import Count 
from app.settings import is_sae
import datetime

import traceback

class ListViewBase(ListView):  
    model = Blog
    context_object_name = 'articleList'
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        try:
            self.cur_page = int(request.GET.get('page', 1))
        except TypeError:
            self.cur_page = 1
        if self.cur_page < 1: self.cur_page = 1
        
        return super(ListViewBase, self).get(request, *args, **kwargs)

    def get_page_range(self, *args, **kwargs):
        queryset = self.get_queryset()
        page_size = self.get_paginate_by(queryset)
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
        after_range_num = 5
        bevor_range_num = 4


        if self.cur_page >= after_range_num:
            page_range = paginator.page_range[self.cur_page - after_range_num:self.cur_page + bevor_range_num]
        else:
            page_range = paginator.page_range[0:int(self.cur_page)+bevor_range_num]

        return page_range

    def get_context_data(self, **kwargs):
        page_range = self.get_page_range()
        kwargs['page_range'] = page_range
        return super(ListView, self).get_context_data(**kwargs)
         

class IndexListView(ListViewBase):
    paginate_by = 6

    def get_queryset(self):
        querySet = Blog.objects.order_by("-updated").filter(is_valid=1)
        return querySet


class TagsListView(ListViewBase):
    paginate_by = 6

    def get_queryset(self):
        self.tag = self.kwargs.get('tag')
        querySet = Blog.objects.filter(tag_name__in=Tag.objects.filter(tagname=self.tag), is_valid=1).order_by("-updated")
        return querySet

    def get_context_data(self, **kwargs):
        kwargs['listname'] = u'Tag of %s' % self.tag
        kwargs['title'] = self.tag + ' | '
        return super(TagsListView, self).get_context_data(**kwargs)
    

class BlogDetailView(DetailView):
    model = Blog
    template_name="page.html"
    slug_field = 'title'
    context_object_name = 'page'


class ArchiveListView(ListView):
    model = Blog
    template_name="archive.html"
    context_object_name = 'archive_items'

    def get_src(self):
        querySet = Blog.objects.all().filter(is_valid=1)
        return querySet

    def get_queryset(self):
        year = datetime.datetime.now().year
        archive_items = {}
        querySet = self.get_src()
        for year in range(year, year-11,-1):
            month_items = {}
            if not querySet.filter(created__year=year): continue

            for month in range(12,0,-1):
                month_blogs=querySet.filter(created__year=year, created__month=month).order_by("-created")
                if not month_blogs: continue
                month_items[month] = month_blogs

            month_items = sorted(month_items.iteritems(), key = lambda asd:asd[0], reverse = True) #排序
            archive_items[year] = month_items

        archive_items = sorted(archive_items.iteritems(), key = lambda asd:asd[0], reverse = True) #排序
        return archive_items

    def get_context_data(self, **kwargs):
        q = self.get_src()
        kwargs['blog_count'] = len(q)
        return super(ArchiveListView, self).get_context_data(**kwargs)



class TagsPageListView(ListView):
    model = Tag
    template_name="tags.html"
    context_object_name = 'tags_items'

    def get_src(self):
        blog_tags = Blog.objects.filter(is_valid=1).values('tag_name').annotate(dcount=Count('tag_name'))
        return blog_tags
    
    def get_queryset(self, **kwargs):
        blog_tags = self.get_src()
        tags = dict([ (x.id,x.tagname) for x in Tag.objects.all() ])
        tags_items = dict( [ (tags[tag["tag_name"]],tag["dcount"]) for tag in blog_tags if tag["tag_name"] ] )
        tags_items = sorted(tags_items.iteritems(), key = lambda asd:asd[1], reverse = True)

        return tags_items


def download(request, offset):
    """Download markdown File. 
    由于SAE不能fileopen所以单独以text/plain 来Response。"""

    blog = get_object_or_404(Blog, id=offset)

    #if is_sae: 
    return HttpResponse(blog.get_full_content().encode('GB18030'), content_type='text/plain')

    with open(u'static/blog/downloads/markdown_%s.md' % offset, 'w') as f:
        f.write(blog.get_full_content().encode('utf-8'))

    return HttpResponseRedirect(u'/static/blog/downloads/markdown_%s.md' % offset)


def error500(request):
    raise Http500()


def error404(request):
    return render_to_response('404.html', { 'page' : ''})
