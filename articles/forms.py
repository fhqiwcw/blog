'''
Created on 2012-4-23

@author: zhaojun
'''
from django import forms
class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField()
    icon = forms.CharField(max_length=100)
    category = forms.IntegerField()
