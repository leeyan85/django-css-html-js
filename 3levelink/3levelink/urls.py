#_*_coding:utf8_*_
from django.conf.urls import patterns, include, url
#from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoProject1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$/', Index),
    #url(r'^index/', views.Index),   
    #(r'^auth/$', views.Auth),
    url(r'^app01/', include('app01.urls')),
)



