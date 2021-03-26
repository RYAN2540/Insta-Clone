from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length = 30)
    caption = models.TextField(blank= True)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="posts")


