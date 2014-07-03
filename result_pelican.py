#!/bin/env python


from blog.models import Blog
from os import path

result_dir = '/data/scripts/backup/results'

all_blog = Blog.objects.all()



for i in all_blog:
    if i.is_valid:
       
        bf = open(path.join(result_dir, i.title + '.md'), 'w')
        bf.write("Title: %s\n" % i.title.encode('utf-8'))
        bf.write("Date: %s\n" % i.created.strftime('%Y-%m-%d %H:%M'))
        bf.write("Category: blog\n")
        bf.write("Tags: %s\n" % i.Tag_List().encode('utf-8'))
        bf.write("Slug: %s\n" % i.slug)
        bf.write("Author: JackeyGao\n\n\n")
        
        bf.write(i.get_full_content().encode("utf-8"))
        bf.close()

