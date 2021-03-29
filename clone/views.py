from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from .forms import UploadImageForm


@login_required(login_url='/accounts/login/')
def home(request):
    title= "Instagram"
    images = Images.objects.all()
    comments = Comment.objects.all()
    return render(request, 'home.html', {"images": images, "comments": comments})

def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
def upload_image(request):
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = request.user
            image.save()
        return redirect('home')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {"form": form})
