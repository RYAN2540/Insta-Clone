from .models import Image,Comment, Profile
from django.forms import ModelForm

class UploadImageForm(ModelForm):
    class Meta :
        model = Image
        exclude = ['profile', 'post_date', 'likes']

class EditBioForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']

class UnfollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']