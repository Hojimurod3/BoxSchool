from django.test import TestCase

# Create your tests here.
import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Teacher, Post, Video
from .serializers import TeacherSerializer, PostSerializer, VideoSerializer

class TeacherAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_data = {
            "name": "Иван",
            "surname": "Иванов",
            "age": "30",
            "information": "Преподаватель информатики"
        }
        self.teacher = Teacher.objects.create(**self.teacher_data)

    def test_create_teacher(self):
        url = reverse('teacher-list-create')
        response = self.client.post(url, self.teacher_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_teacher_detail(self):
        url = reverse('teacher-detail', kwargs={'pk': self.teacher.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.teacher.name)
        self.assertEqual(response.data['surname'], self.teacher.surname)

    def test_create_post_for_teacher(self):
        url = reverse('teacher-posts-list', kwargs={'pk': self.teacher.pk})
        post_data = {
            "title": "Новый пост",
            "information": "Текст нового поста"
        }
        response = self.client.post(url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_video_for_teacher(self):
        url = reverse('teacher-videos-list', kwargs={'pk': self.teacher.pk})
        video_data = {
            "video": "ссылка_на_видео.mp4"
        }
        response = self.client.post(url, video_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        post = Post.objects.create(teacher=self.teacher, title='Test Post', information='Test Information')
        url = reverse('post-detail', kwargs={'pk': post.pk})
        updated_data = {
            "title": "Updated Title",
            "information": "Updated Information"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
        self.assertEqual(response.data['information'], updated_data['information'])

    def test_delete_video(self):
        video = Video.objects.create(teacher=self.teacher, video='test_video.mp4')
        url = reverse('video-detail', kwargs={'pk': video.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
