from django.contrib import admin
from .models import Profile, Comment, Image, Follow

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Follow)
