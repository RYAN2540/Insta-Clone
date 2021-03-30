from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment, Follow
from .forms import CreateProfileForm,UploadImageForm, EditBioForm, FollowForm, UnfollowForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect(home)

    else:
        form = CreateProfileForm()
    return render(request, 'create-profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def home(request):
    title= "Instagram"
    current_user =request.user
    try:
        logged_in = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    timeline_images = []
    current_images = Image.objects.filter(profile = logged_in)
    for current_image in current_images:
        timeline_images.append(current_image.id)

    current_following = Follow.objects.filter(follower = logged_in)
    for following in current_following:
        following_profile = following.followed
        following_images = Image.get_profile_images(following_profile)
        for image in following_images:
            timeline_images.append(image.id)

    display_images= Image.objects.filter(pk__in = timeline_images).order_by('-post_date')
    liked = False
    for i in display_images:
        image = Image.objects.get(pk=i.id)
        liked = False
        if image.likes.filter(id =request.user.id).exists():
            liked = True
    comments = Comment.objects.all()
    comments_count= comments.count()
    
    suggestions = Profile.objects.all()[:4]
    print("IMAGES")
    print(len(display_images))
    return render(request, 'home.html', {"images": display_images,"liked" : liked, "comments": comments, "title": title, "suggestions": suggestions})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    title = "Profile"
    current_user = request.user
    prof_id = current_user.id - 1
    pr_id= int(profile_id) - 1
    username = current_user.username
    print(pr_id)
    # user = User.objects.filter(username=username)
    # user_id=request.user.id
    # profile = Profile.objects.get(id = prof_id)
    # profile = Profile.search_user(username)
    # print("logged_in user")
    # print(profile[0].username)
    try:
        # profile = User.objects.filter(id = profile_id)
        # profile = Profile.search_user(username)
        profile = Profile.objects.get(user =current_user)
        print("followers")
        print(profile[0].following)
    except Profile.DoesNotExist:
        raise Http404()
    try:
        profile_following = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    try:
        profile_followed = Profile.objects.get(id = profile_id)
    except Profile.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        if 'follow' in request.POST:
            form = FollowForm(request.POST)
            if form.is_valid():
                this_follow = form.save(commit=False)
                this_follow.followed=profile_followed
                this_follow.follower=profile_following
                this_follow.save()
                set_of_followers=Follow.objects.filter(followed = profile_followed)
                num_of_followers=len(set_of_followers)
                profile_followed.followers=num_of_followers
                profile_followed.save()
                set_of_following=Follow.objects.filter(follower = profile_following)
                num_of_following=len(set_of_following)
                profile_following.following=num_of_following
                profile_following.save()
            return HttpResponseRedirect(f'/profile/{profile_id}')

        elif 'unfollow' in request.POST:
            form = UnfollowForm(request.POST)
            if form.is_valid():
                this_unfollow = form.save(commit=False)
                is_unfollow = Follow.objects.filter(followed = profile_followed, follower = profile_following)
                is_unfollow.delete()                
                set_of_followers=Follow.objects.filter(followed = profile_followed)
                num_of_followers=len(set_of_followers)
                profile_followed.followers=num_of_followers
                profile_followed.save()
                set_of_following=Follow.objects.filter(follower = profile_following)
                num_of_following=len(set_of_following)
                profile_following.following=num_of_following
                profile_following.save()
            return HttpResponseRedirect(f'/profile/{profile_id}')



    else:
        form_follow = FollowForm()
        form_unfollow = UnfollowForm()

    images = Image.objects.filter(profile = profile).order_by('-posted')
    images = Image.get_profile_images(profile = profile)
    images = Image.objects.filter(profile = profile).order_by('-posted')
    posts = images.count()  

    is_following = Follow.objects.filter(followed = profile_followed, follower = profile_following) 
    comments = Comment.objects.order_by('-posted')   

    if is_following:
        return render(request, 'profile/profile.html', {"profile": profile, "images": images, "comments":comments, "unfollow_form": form_unfollow, "posts": posts, "title": title})

    return render(request, 'profile/profile.html', {"profile": profile, "images": images, "comments":comments, "follow_form": form_follow, "posts": posts, "title": title})
    # return render(request, 'profile/profile.html')

@login_required(login_url='/accounts/login/')
def upload_image(request):
    title = "Instagram | Upload image"
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = profile
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

def like_image(request,image_id):
    image = Image.objects.get(pk=image_id)
    liked = False
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if image.likes.filter(id=profile.id).exists():
        image.likes.remove(profile)
        liked = False
    else:
        image.likes.add(profile)
        liked = True
    return HttpResponseRedirect(reverse('home'))

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