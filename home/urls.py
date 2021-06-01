"""extreme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('course1', views.course1, name='course1'),
    path('course2', views.course2, name='course2'),
    path('batch', views.batch, name='batch'),
    path('branch', views.branche, name='branch'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('office', views.office, name='office'),
    path('search', views.search, name='search'),
    
    
]