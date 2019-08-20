from django.urls import path,include

import  blog.views
from django.conf.urls import url

urlpatterns=[
    path('hello_world',blog.views.hello_world),
    path('content',blog.views.article_content),
    url(r'^index/', blog.views.index),
    url(r'^index2/', blog.views.index2),
    #url(r'all',blog.all,name='all'),
]