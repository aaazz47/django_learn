# blog/urls.py
from django.conf.urls import url

from . import views

# 设置URL的名空间
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.BlogIndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<name>.*)/$', views.CategoryView.as_view(), name='category'),
]
