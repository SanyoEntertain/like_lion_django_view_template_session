"""
URL configuration for ex_django_serengeti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import django.contrib.auth.urls
from django.contrib import admin
from django.urls import include, path
from account.views import UserCreateView, UserCreateDoneTemplateView
from main.views import root

urlpatterns = [
    path('', root, name='root'),
    path('admin/', admin.site.urls),
    path('', include('ping_pong.urls')),
    # django.contrib.auth.urls.urlpatterns를 확인해보자.
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTemplateView.as_view(), name='register_done'),
    path('article/', include('article.urls')),
]
