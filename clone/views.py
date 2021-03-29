from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from .forms import UploadImageForm


@login_required(login_url='/accounts/login/')
def home(request):
    title= "Instagram"
    images = Image.objects.all()
    comments = Comment.objects.all()
    return render(request, 'home.html', {"images": images, "comments": comments, "title": title})

def profile(request):
    title = "Profile"
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    images = Image.get_profile_images(current_user)
    posts = images.count()
    print(posts)
    return render(request, 'profile/profile.html', {"profile" : profile, "images":images, "posts": posts, "title": title})

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
        return render(request, 'upload_image.html', {"form": form, "title": title})

@login_required
def search(request):
    if "user" in request.GET and request.GET["user"]:
        searched_user = request.GET.get("user")
        profile = Profile.search_user(searched_user)
        title = profile[0].username + " | Instagram"
        print(profile[0].username)
        images = Image.get_profile_images(profile[0].id)
        posts = images.count()
        print(posts)
        return render(request, 'profile/profile.html', {"profile" : profile, "images":images, "posts": posts, "title": title})
    else:
        message = "You haven't searched for any term"
        return render(request,'profile/profile.html', {"message": message})

@login_required
def comment(request, image_id):
    image = Image.objects.get(pk=image_id)
    content= request.GET.get("comment")
    print(content)
    user = request.user
    comment = Comment( image = image, content = content, user = user)
    comment.save_comment()

    return redirect('home')