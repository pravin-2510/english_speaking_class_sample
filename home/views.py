from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from home.models import Enquire
from django.contrib import messages
from blog.models import Post

# Create your views here.


def home(request):
    context = {"home_page": "active"}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    return render(request, 'home/home.html')


def course1(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    return render(request, 'home/course1.html')


def course2(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    return render(request, 'home/course2.html')


def branche(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    return render(request, 'home/branch.html')


def batch(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    return render(request, 'home/batch.html')


def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, 'home/contact.html')


def office(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, ' Please Enter Valid Details.')
        else:
            enquire = Enquire(name=name, email=email,
                              phone=phone, content=content)
            enquire.save()
            messages.success(
                request, ' Your Detail is Successfully Submitted.')
    return render(request, 'home/office.html')


def search(request):
    query = request.GET['search']
    if len(query) >= 78:
        Posts = Post.objects.none()
    else:
        Poststitle = Post.objects.filter(title__icontains = query)
        Postscontent = Post.objects.filter(content__icontains = query)
        Posts = Poststitle.union(Postscontent)
        if Posts.count() == 0:
            messages.warning(request, "No Search Result Found")
        params = {'Posts':Posts, 'query':query}
        return render(request, 'home/search.html',params)
    
