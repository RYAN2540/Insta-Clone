from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^email/$',views.email,name = 'email'),
    url(r'^create_profile/$',views.create_profile,name = 'create_profile'),
    url(r'^profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
    url(r'^upload/image$', views.upload_image, name = "upload_image"),
    url(r'^search/',views.search,name ='search'),
    url(r'^like/(?P<image_id>\d+)', views.like_image, name = 'like_image'),
    url(r'^comment/(?P<image_id>\d+)', views.comment,name = "comment"),
    url(r'^profile/edit$', views.profile_edit,name = 'profile_edit'),
]