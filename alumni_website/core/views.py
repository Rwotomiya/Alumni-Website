from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, JobPosting, MentorshipRequest
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm,JobPostingForm, MentorshipRequestForm
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

def job_postings(request):
    jobs = JobPosting.objects.all().order_by('-posted_on')
    return render(request, 'jobs/job_postings.html', {'jobs': jobs})

def job_details(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    return render(request, 'jobs/job_details.html', {'job': job})

def mentorship_requests(request):
    requests = MentorshipRequest.objects.all().order_by('-requested_on')
    return render(request, 'mentorship/requests.html', {'requests': requests})
    
# Job Posting Form View
@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user  # Assign the current user as the poster
            job.save()
            return redirect('job_postings')  # Redirect to the job postings page
    else:
        form = JobPostingForm()
    return render(request, 'jobs/post_job.html', {'form': form})

# Mentorship Request Form View
@login_required
def request_mentorship(request):
    if request.method == 'POST':
        form = MentorshipRequestForm(request.POST)
        if form.is_valid():
            mentorship = form.save(commit=False)
            mentorship.requested_by = request.user  # Assign the current user as the requester
            mentorship.save()
            return redirect('mentorship_requests')  # Redirect to the mentorship requests page
    else:
        form = MentorshipRequestForm()
    return render(request, 'mentorship/request_mentorship.html', {'form': form})

# Edit Job Posting
@login_required
def edit_job(request, pk):
    job = get_object_or_404(JobPosting, pk=pk, posted_by=request.user)
    if request.method == 'POST':
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_postings')
    else:
        form = JobPostingForm(instance=job)
    return render(request, 'jobs/edit_job.html', {'form': form})

# Delete Job Posting
@login_required
def delete_job(request, pk):
    job = get_object_or_404(JobPosting, pk=pk, posted_by=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('job_postings')
    return render(request, 'jobs/delete_job.html', {'job': job})

def job_postings(request):
    jobs = JobPosting.objects.all().order_by('-posted_on')
    query = request.GET.get('q')
    job_type = request.GET.get('type')
    if query:
        jobs = jobs.filter(title__icontains=query)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    return render(request, 'jobs/job_postings.html', {'jobs': jobs})
