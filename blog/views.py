from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blogHome(request):
    user_list = Post.objects.all().order_by('-Created_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    Posts = Post.objects.all().order_by('-Created_date')
    context = { 'Posts' : Posts}
    post_ids = Post.objects.all()
    context = {'post_ids': post_ids}
    return render(request,'blog/bloghome.html', { 'users': users,'Posts': Posts, 'post_ids': post_ids })
def blogPost(request, slug):
    blogposts = Post.objects.filter(slug = slug).first()
    context = {'blogposts': blogposts}
    Posts = Post.objects.all().order_by('-Created_date')
    context = { 'Posts' : Posts}
    post_ids = Post.objects.all()
    context = {'post_ids': post_ids}
    return render(request,'blog/blogPost.html', { 'blogposts': blogposts,'Posts': Posts, 'post_ids': post_ids })
    