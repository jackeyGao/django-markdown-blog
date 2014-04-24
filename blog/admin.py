#coding=UTF-8
from django.contrib import admin
from blog.models import *


class BlogAdmin(admin.ModelAdmin):
    list_display  = ('title','created','updated','is_reply','is_valid','Tag_List')
    search_fields = ('title','content')
    list_filter   = ('is_reply','is_valid','updated')
    list_display_links = ('title',)
    ordering = ('-created',)
    date_hierarchy = 'updated' 

    #filter_horizontal = ('tag_name',)  

#此处控制后台admin编辑器是否使用tinyMCE
#    class Media:
#        js = [
#            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
#            '/static/grappelli/tinymce_setup/tinymce_setup.js ',
#        ]


class TagAdmin(admin.ModelAdmin):
    list_display = ('tagname',)
    search_fields = ('tagname',)



admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
