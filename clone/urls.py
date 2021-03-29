from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^upload/image/$', views.upload_image, name = "upload_image"),
    url(r'^user/(?P<username>)',views.user,name ='user'),
]