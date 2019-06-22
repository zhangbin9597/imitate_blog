import markdown
from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404
from .models import Post,Tag,Category
from comments.forms import CommentForm

class IndexView(ListView):
    pass
def index(request):
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form = CommentForm()
    #获取这篇post下的所有评论
    comment_list = post.comment_set.all()
    context={
        'post':post,
        'form':form,
        'comment_list':comment_list,
    }
    return render(request,'blog/detail.html',context=context)
def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=category).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

class PostDetailView(View):
    pass

class ArchivesView(View):
    pass
class CategoryView(View):
    pass
class TagView(View):
    pass
