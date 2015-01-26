#_*_coding:utf8_*_
from django.conf.urls import patterns, url
#from django.contrib import admin
import line3level

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoProject1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$/', Index),
    #url(r'^index/', views.Index),   
    #(r'^auth/$', views.Auth),
    url(r'^link', line3level.ThreeLevel),
    url(r'^getRegion/$',line3level.SelelectRegion),   
    url(r'^RegionInfo/$',line3level.RegionInfo),
)



