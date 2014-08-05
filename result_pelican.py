#!/bin/env python
import os, sys

prodir = os.getcwd()
sys.path.append(prodir)

reload(sys)
sys.setdefaultencoding('utf8')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from blog.models import Blog


result_dir = '/tmp'

all_blog = Blog.objects.all()



for i in all_blog:
    if i.is_valid:
       
        bf = open(os.path.join(result_dir, i.title + '.md'), 'w')
        bf.write("Title: %s\n" % i.title.encode('utf-8'))
        bf.write("Date: %s\n" % i.created.strftime('%Y-%m-%d %H:%M'))
        bf.write("Category: blog\n")
        bf.write("Tags: %s\n" % i.Tag_List().encode('utf-8'))
        bf.write("Slug: %s\n" % i.slug)
        bf.write("Author: JackeyGao\n\n\n")
        
        bf.write(i.get_full_content().encode("utf-8"))
        bf.close()

