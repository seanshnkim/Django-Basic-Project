"""do_it_django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    #1. path('blog/') : 웹 사이트 방문자가 주소 창에 도메인 뒤에 /blog/를 붙여서 입력
    #2. 서버는 장고 프로젝트 폴더(do_it_django_prj)의 urls.py에서
    #3. '도메인 뒤에 /blog/가 붙었을 때에는 blog/urls.py에서 처리한다' -> blog/urls.py로 접근'''

]
