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