from rest_framework import serializers
from .models import Teacher, Video , Post

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'age', 'information']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'information']