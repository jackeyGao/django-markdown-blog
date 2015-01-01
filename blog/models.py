# -*- coding:utf-8 -*-
from django.db import models
from app.settings import blog_template, url_list
#from wmd import models as wmd_models

# Create your models here.


class Tag(models.Model):
    tagname = models.CharField(u'标签名称', max_length=50)

    def __unicode__(self):
        return self.tagname


class Blog(models.Model):
    title     = models.CharField(u'日志标题',max_length=50)
    slug      = models.CharField(u'日志URL',max_length=45)
    content   = models.TextField(u'日志内容')
    #content   = wmd_models.MarkDownField(u'日志内容')
    created   = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated   = models.DateTimeField(u'更新时间', auto_now=True)
    tag_name  = models.ManyToManyField(Tag)
    is_reply  = models.BooleanField(u'是否评论')
    is_valid  = models.BooleanField(u'是否有效')

    def __unicode__(self):
        return self.title

    def Tag_List(self):
        return ','.join([ x.tagname for x in self.tag_name.all() ])
    
    def get_absolute_url(self):
        return u'/page/%s/' % self.slug

    def get_full_content(self):
        if self.is_valid:
            page_full_url = self.get_absolute_url()
             
            return self.content + "\n\n" + blog_template % page_full_url + "\n\n" + '\n'.join(url_list)

        else:
            return self.content


class Photo(models.Model):
    image = models.ImageField(upload_to='media')
 
     


