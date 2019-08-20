"""datacheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import blog.views

try:
    from django.conf.urls.defaults import url
except:
    from django.conf.urls import url, include  # higher version of django

blog_patterns = [
    url(r'^index2', blog.views.index2),
    url(r'^all', blog.views.all)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog_patterns))
]

urlpatterns += staticfiles_urlpatterns()