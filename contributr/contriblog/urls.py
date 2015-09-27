from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^tags/(?P<tag>\S+)$', views.TagDetail.as_view(), name="tag_detail"),
    url(r'^post/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="detail"),
    url(r'^new/$', views.postNew.as_view(), name='postNew'),
    url(r'^post/(?P<slug>\S+)/edit$', views.editForm.as_view(), name="editForm")
    ]
