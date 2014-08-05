#!/bin/env python


import os, sys

prodir = os.getcwd()
sys.path.append(prodir)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from blog.models import Blog


result_dir = '/tmp/'

all_blog = Blog.objects.all()

for i in all_blog:
    if i.is_valid:
        bf = open(os.path.join(result_dir, i.title + '.mdown'), 'w')
        bf.write(i.get_full_content().encode("utf-8"))
        bf.close()

