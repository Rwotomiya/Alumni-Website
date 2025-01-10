from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduation_year = models.CharField(max_length=4)
    profession = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(
        max_length=50,
        choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Remote', 'Remote')],
    )
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    application_link = models.URLField(max_length=500)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class MentorshipRequest(models.Model):
    field_of_interest = models.CharField(max_length=255)
    details = models.TextField()
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mentorship in {self.field_of_interest} by {self.requested_by}"