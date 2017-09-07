from django.conf.urls import url

from .views import (
    CreateUserView,
    UpdateUserView,
    ListUserView,
    DetailUserView,
    ListPostView,
    CreatePostView,
    DetailPostView,
    UpdatePostView)

urlpatterns = [
    url(r'^user/$', ListUserView.as_view(), name='user-list'),
    url(r'^user/registration/$', CreateUserView.as_view(), name='user-create'),
    url(r'^user/(?P<pk>[\w-]+)/$', DetailUserView.as_view(), name='user-detail'),
    url(r'^user/(?P<pk>[\w-]+)/edit$', UpdateUserView.as_view(), name='user-update'),
    url(r'^post/$', ListPostView.as_view(), name='post-list'),
    url(r'^post/create/$', CreatePostView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>[\w-]+)/$', DetailPostView.as_view(), name='post-detail'),
    url(r'^post/(?P<pk>[\w-]+)/edit$', UpdatePostView.as_view(), name='post-update'),
]
