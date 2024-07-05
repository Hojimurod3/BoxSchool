from django.db import models
from config.models import Time


class Video(Time):
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name="video")
    video = models.FileField()


class Teacher(Time):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.CharField(max_length=100)
    information = models.TextField()


class Post(Time):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=255)
    information = models.TextField()

