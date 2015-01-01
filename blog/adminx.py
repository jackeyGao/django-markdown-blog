#coding=UTF-8
#from django.contrib import admin
from blog.models import *
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    global_search_models = [Blog, Tag, Photo]
    global_models_icon = {
        Blog: 'fa fa-laptop', Tag: 'fa fa-cloud', Photo: 'fa fa-cloud'
    }
    menu_style = 'default'#'accordion'
xadmin.site.register(views.CommAdminView, GlobalSetting)



#class BlogAdmin(admin.ModelAdmin):
class BlogAdmin(object):
    list_display  = ('title','created','updated','is_reply','is_valid','Tag_List', 'slug')
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


class TagAdmin(object):
    list_display = ('tagname',)
    search_fields = ('tagname',)

class PhotoAdmin(object):
    list_display = ('image',)


#admin.site.register(Blog, BlogAdmin)
#admin.site.register(Tag, TagAdmin)
#admin.site.register(Photo, PhotoAdmin)


xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Photo, PhotoAdmin)
