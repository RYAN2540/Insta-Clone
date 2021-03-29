from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from .forms import UploadImageForm, EditBioForm
from django.urls import reverse

@login_required(login_url='/accounts/login/')
def home(request):
    title= "Instagram"
    images = Image.objects.all()
    comments = Comment.objects.all()
    comments_count= comments.count()
    print(comments[0].image.id)
    print(comments[1].image)
    print(images[0].id)
    print(images[0].comments)
    return render(request, 'home.html', {"images": images, "comments": comments, "title": title})

@login_required(login_url='/accounts/login/')
def profile(request):
    title = "Profile"
    current_user = request.user
    profile = Profile.search_user(request.user)
    images = Image.get_profile_images(request.user)
    posts = images.count()
    print(posts)
    return render(request, 'profile/profile.html', {"profile" : profile, "images":images, "posts": posts, "title": title})

@login_required(login_url='/accounts/login/')
def upload_image(request):
    title = "Instagram | Upload image"
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

def comment(request, image_id):
    image = Image.objects.get(pk=image_id)
    content= request.GET.get("comment")
    print(content)
    user = request.user
    comment = Comment( image = image, content = content, user = user)
    comment.save_comment()

    return redirect('home')

def like_image(request,id):
    image = Image.objects.get(pk=id)
    liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        liked = False
    else:
        image.likes.add(request.user)
        liked = True 
    return HttpResponseRedirect(reverse('home',args =[int(image.id)]))

def profile_edit(request):
    current_user = request.user
    if request.method == "POST":
        form = EditBioForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data['profile_pic']
            bio  = form.cleaned_data['bio']
            updated_profile = Profile.objects.get(user= current_user)
            updated_profile.profile_pic = profile_pic
            updated_profile.bio = bio
            updated_profile.save()
        return redirect('profile')
    else:
        form = EditBioForm()
    return render(request, 'edit_profile.html', {"form": form})