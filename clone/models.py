from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length = 30)
    caption = models.TextField(blank= True)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="posts")
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    def like_count(self):
        return self.likes.count()

    @classmethod
    def get_profile_images(cls,profile):
        return cls.objects.filter(profile = profile)

    class Meta:
        ordering = ['-post_date']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio =  models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def search_user(cls,username): 
        return User.objects.filter(username = username)

class Comment(models.Model):
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete= models.CASCADE, related_name = "comments")

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls,image):
        return cls.objects.filter(image =image)

    class Meta:
        ordering = ['-post_date']

class Follow(models.Model): 
    posted = models.DateTimeField(auto_now_add=True)
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_followed')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_following')

    def __str__(self):
        return self.pk