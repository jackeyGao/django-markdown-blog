# -*- coding:utf-8 -*-
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response,get_object_or_404 
from django.core.paginator import Paginator
from blog.models import Blog, Tag

from django.db.models import Count 
from app.settings import is_sae
import datetime

import traceback

def list(quearySet, listname, page_number):
    """分页函数"""

    after_range_num = 5
    bevor_range_num = 4

    all_logs = quearySet
    paginator = Paginator(all_logs, after_range_num)
    
    try:  
        articleList = paginator.page(page_number)
    except Exception,e:  
        listname='页码%s不存在, 已经返回首页.' % page_number
        articleList = paginator.page(1)
    # Get logs & Paginator

    if page_number >= after_range_num:
        page_range = paginator.page_range[page_number - after_range_num:page_number + bevor_range_num]
    else:
        page_range = paginator.page_range[0:int(page_number)+bevor_range_num]
    return render_to_response('list.html', locals())


def getPageNumber(request):
    """获取page参数（页码）"""
    try:
        page_number=int(request.GET.get('page')) if request.GET.get('page') else 1
        return page_number
    except ValueError:
        raise Http404()


def tagSearchList(request, keyword):
    """Tags List View"""
    item_url = '/tagSearchList/%s/' % keyword
    page_number = getPageNumber(request)
    quearySet = Blog.objects.filter(tag_name__in=Tag.objects.filter(tagname=keyword), is_valid=1).order_by("-updated")

    return list(quearySet, listname=u'Tag of %s'%keyword,  page_number=page_number)


def home(request,page_number=1):
    """All Blog List View"""
    page_number = getPageNumber(request)
    quearySet = Blog.objects.order_by("-updated").filter(is_valid=1)

    return list(quearySet,listname=u"Home", page_number=page_number)


def page(request, offset):
    """Blog Detail View"""
    page = get_object_or_404(Blog, title=offset)

    return render_to_response('page.html', locals())


def archive(request):
    """Archive View"""

    year = datetime.datetime.now().year
    archive_items = {}
    querySet = Blog.objects.all().filter(is_valid=1)
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
    return render_to_response('archive.html', locals())


def tag(request):
    """Tag View"""

    tag_count = Blog.objects.filter(is_valid=1).values('tag_name').annotate(dcount=Count('tag_name'))
    tags = dict([ (x.id,x.tagname) for x in Tag.objects.all() ])
    tags_items = dict( [ (tags[tag["tag_name"]],tag["dcount"]) for tag in tag_count if tag["tag_name"] ] )
    tags_items = sorted(tags_items.iteritems(), key = lambda asd:asd[1], reverse = True) #排序

    return render_to_response('tags.html', locals()) 


def search(request):
    return render_to_response('search.html', locals())


def download(request, offset):
    """Download markdown File. 
    由于SAE不能fileopen所以单独以text/plain 来Response。"""

    blog = get_object_or_404(Blog, id=offset)

    if is_sae: return HttpResponse(blog.get_full_content().encode('GB18030'), content_type='text/plain')

    with open(u'static/blog/downloads/markdown_%s.md' % offset, 'w') as f:
        f.write(blog.get_full_content().encode('utf-8'))

    return HttpResponseRedirect(u'/static/blog/downloads/markdown_%s.md' % offset)


def error500(request):
    raise Http500()


def error404(request):
    return render_to_response('404.html', { 'page' : ''})
