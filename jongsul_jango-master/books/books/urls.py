"""books URL Configuration

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
from django.conf.urls import url, include
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^usermanage/', include(('usermanage.urls','usernamage'),namespace="usermanage")),
    url(r'^check/', include(('check.urls','check'),namespace="check")),
    url(r'^reservation/', include(('reservation.urls','revervation'), namespace="reservation")),
    #   reservation result url 작성부탁드려요. 그리고 이 url base.html에 reservation result라고 써진부분에 넣어주세요.

]
