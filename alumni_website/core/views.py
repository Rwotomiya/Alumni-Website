from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from django.db.models import Q
from .models import NewsPost

def news_list(request):
    news = NewsPost.objects.all().order_by('-date_posted')
    return render(request, 'core/news_list.html', {'news': news})

def alumni_directory(request):
    query = request.GET.get('q')
    if query:
        alumni = Profile.objects.filter(
            Q(user__username__icontains=query) |
            Q(graduation_year__icontains=query)
        )
    else:
        alumni = Profile.objects.all()
    return render(request, 'core/directory.html', {'alumni': alumni})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'core/profile.html', {'profile': request.user.profile})

def alumni_directory(request):
    alumni = Profile.objects.all()
    return render(request, 'core/directory.html', {'alumni': alumni})

def homepage(request):
    return render(request, 'core/homepage.html')
