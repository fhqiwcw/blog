# -*- coding: utf-8 -*-
from django.db import models

# Category是文章的分类
class Category(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '[Category name=' + self.name + ']'
    
    class Meta:
        db_table = 'category' #表名为category

# Post是博文的实体类
class Post(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    icon = models.CharField(max_length=100)
    createdate = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return '[Post title=' + self.title\
            + ',content=' + self.content[:30]\
            + ',icon=' + self.icon\
            + ',createdate=' + str(self.createdate) + ']'
    
    class Meta:
        db_table = 'post' #表名为post

