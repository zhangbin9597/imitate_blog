from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comment/post/(?P<pk>[0-9]+)/$',views.post_comment,name='post_comment'),
    # url(r'^comment/post/(?P<pk>[0-9]+)/$',views.CommentView.as_view(),name='post_comment'),
]