from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^email/$', views.email, name='email'),
    re_path(r'^create_profile/$', views.create_profile, name='create_profile'),
    re_path(r'^profile/(?P<profile_id>\d+)', views.profile, name='profile'),
    re_path(r'^upload/image$', views.upload_image, name="upload_image"),
    re_path(r'^search/', views.search, name='search'),
    re_path(r'^like/(?P<image_id>\d+)', views.like_image, name='like_image'),
    re_path(r'^comment/(?P<image_id>\d+)', views.comment, name="comment"),
    re_path(r'^profile/edit$', views.profile_edit, name='profile_edit'),
]
