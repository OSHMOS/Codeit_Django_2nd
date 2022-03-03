from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {"posts" : posts}
    return render(request, 'posts/post_list.html', ctx)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    ctx = {"post" : post}
    return render(request, 'posts/post_detail.html', ctx)