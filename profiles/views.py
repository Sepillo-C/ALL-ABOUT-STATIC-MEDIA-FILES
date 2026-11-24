from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Profile, Post
from .forms import ProfileForm


def profile_view(request):
    profile, created = Profile.objects.get_or_create(
        pk=1,
        defaults={'name': 'Your Name'}
    )

    posts = profile.posts.all()

    return render(request, 'profile/profile.html', {
        'profile': profile,
        'posts': posts
    })


def edit_profile(request):
    profile, created = Profile.objects.get_or_create(
        pk=1,
        defaults={'name': 'Your Name'}
    )

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {
        'form': form,
        'profile': profile
    })


@require_POST
def create_post(request):
    profile, created = Profile.objects.get_or_create(
        pk=1,
        defaults={'name': 'Your Name'}
    )

    content = request.POST.get('content', '').strip()

    if content:
        Post.objects.create(
            profile=profile,
            content=content
        )

    return redirect('profile')


@require_POST
def delete_post(request, post_id):
    post = Post.objects.filter(
        id=post_id,
        profile_id=1
    ).first()

    if post:
        post.delete()

    return redirect('profile')