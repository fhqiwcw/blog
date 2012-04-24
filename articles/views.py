# -*- coding:utf-8 -*-
# Create your views here.
from articles.forms import PostForm
from articles.models import Post, Category
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse


def index(request):
    '''
    博客首页
    '''
    categorys = Category.objects.all()
    model_map = {'categorys': categorys}
    return render_to_response('index.html', model_map, context_instance=RequestContext(request))

def show_post_detail(request, post_id):
    '''
    由id得到一条博客内容
    '''
    try:
#        post = Post.objects.get(id=post_id)
        post = get_object_or_404(Post, pk=post_id)
    except Post.DoesNotExist:
        return Http404
    
    return HttpResponse(post)

def insert(request):
    '''
    打开发布博客，为发布博客页面准备上下文
    '''
    return render_to_response('insert.html', {}, context_instance=RequestContext(request))

def add(request):
    '''
    在数据库中插入一条博客
    '''
    title = request.POST['title']
    content = request.POST['content']
    icon = request.POST['icon']
    category_id = request.POST['category_id']
    c = Category.objects.get(id=category_id)
    post = Post(title=title, content=content, icon=icon, category=c)
    post.save()
    return HttpResponse('success');

def open_post_form(request):
    form = PostForm()
    return render_to_response('post_form.html', {'form':form}, context_instance=RequestContext(request))

def save_post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            #save to db
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.icon = form.cleaned_data['icon']
            post.category = Category.objects.get(pk=form.cleaned_data['category'])
            post.save()
            return HttpResponseRedirect(reverse(show_post_detail, args=[post.id]))
        else:
            return HttpResponse('Failed')
        
    else:
        return HttpResponse('Failed')
