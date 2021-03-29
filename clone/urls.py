from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^upload/image$', views.upload_image, name = "upload_image"),
    url(r'^search/',views.search,name ='search'),
    url(r'^like/<int:id>$', views.like_image, name = 'like_image'),
    url(r'^comment/(?P<image_id>\d+)', views.comment,name = "comment"),
    url(r'^profile/edit$', views.profile_edit,name = 'profile_edit'),
]