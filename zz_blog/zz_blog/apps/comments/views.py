from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from blog.models import Post
from .models import Comment
from .forms import CommentForm
# Create your views here.

class CommentView(View):
    def get(self,request,pk):
        pass

def post_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method =='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list =post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
        return render(request,'blog/detail.html',context=context)
    return redirect(post)


