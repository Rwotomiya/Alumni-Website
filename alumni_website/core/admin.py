from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Profile
# Register your models here.
admin.site.register(Profile)

admin.site.site_header = "LACOBA Administration"
admin.site.site_title = "LOCABA Admin Portal"
admin.site.index_title = "Welcome to LACOBA Admin"

