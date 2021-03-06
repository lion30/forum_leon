"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

import django
from django.conf.urls import url, include
from django.contrib import admin
from forum.views import htmltemplate, index, register, test
from usercenter.views import activate

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^htmltemplate/$', htmltemplate),
	url(r'^$', index),
	url(r'^article/',include('article.urls')),
	url(r'^comment/',include('comment.urls')),
	url(r'^message/',include('message.urls')),
	url(r'^register/$', register),
	url(r'^test/$', test),
	url(r'^activate/(?P<code>\w+)$', activate),
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^usercenter/', include('usercenter.urls')),
	url(r'^ueditor/', include('DjangoUeditor.urls'))
]

admin.site.disable_action('delete_selected')