'''
Created on 2012-4-18

@author: zhaojun
'''
from articles import models
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name',)
    
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'content', 'icon']
    list_display = ('id', 'title', 'category', 'content', 'icon', 'createdate',)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
