"""
URL configuration for Mascotas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from Bd_mascotas import views as views_mascotas
from Bd_mascotas.views import BlogListView, BlogCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_mascotas.index),
    path('index/', views_mascotas.index),
    path('about/', views_mascotas.about),
    path('contact/', views_mascotas.contact),
    path('products/', views_mascotas.products),
    path('service/', views_mascotas.service),
    path('registration/', views_mascotas.registration),
    path('single/<id>/', views_mascotas.single),
    
    #crud post
    path('blog/',  BlogListView.as_view(), name="ListarPost"), 
    path('CrearPost/',  BlogCreate.as_view(), name="CrearPost")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
