from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.post_list, name='post_list_by_category'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post_slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<post_id>\d+)/pdf/$', views.post_pdf, name='post_pdf'),
]