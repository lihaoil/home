"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from myapp import uploadView
from myapp import uploadView2
from myapp import views
from myapp import view1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog),
    path('auth/', views.get_token),
    path('upload/', uploadView.upload),
    path('uploadFile/', uploadView2.uploadFile),
    path('article/', views.add_article),
    path('article/<int:article_id>', views.modify_article),
]