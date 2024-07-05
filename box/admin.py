from django.contrib import admin
from .models import Video, Post, Teacher

admin.site.register([Video, Post, Teacher])