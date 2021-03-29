from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title= "Instagram"
    images = Images.objects.all()
    comments = Comment.objects.all()
    return render(request, 'home.html', {"images": images, "comments": comments})

def profile(request):
    return render(request, 'profile.html')