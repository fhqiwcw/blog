# -*- coding:utf-8 -*-
'''
Created on 2012-4-18

@author: zhaojun
'''
from articles.models import Post
from django.conf.urls import url, patterns
from django.views.generic.detail import DetailView
urlpatterns = patterns('articles.views',
                       url(r'^index', 'index'),
                       url(r'^(?P<post_id>\d+)/$', 'show_post_detail'),
                       url(r'^insert', 'insert'),
                       url(r'^add', 'add'),
                       url(r'^form', 'open_post_form'),
                       url(r'^save/$', 'save_post_form'),
                       )

'''
便捷显示内容
'''
'''
urlpatterns += patterns('',
                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(
                                              model=Post,
                                              template_name='detail.html')
                           ),
                        )
'''
