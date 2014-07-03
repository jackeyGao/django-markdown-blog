#!/bin/env python


from blog.models import Blog
from os import path

result_dir = '/data/scripts/backup/data/blog/'

all_blog = Blog.objects.all()

for i in all_blog:
    if i.is_valid:
        bf = open(path.join(result_dir, i.title + '.mdown'), 'w')
        bf.write(i.get_full_content().encode("utf-8"))
        bf.close()

