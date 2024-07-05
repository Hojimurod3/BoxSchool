from django.urls import path
from .views import TeacherDetail, TeacherPostsList, TeacherVideosList, PostDetail, VideoDetail, TeacherListCreate, PostsListCreate, VideoListCreate

urlpatterns = [
    path('teachers/', TeacherListCreate.as_view()),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    path('teachers/<int:pk>/posts/', TeacherPostsList.as_view(), name='teacher-posts-list'),
    path('teachers/<int:pk>/videos/', TeacherVideosList.as_view(), name='teacher-videos-list'),
    path('posts/', PostsListCreate.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('videos/', VideoListCreate.as_view()),
    path('videos/<int:pk>/', VideoDetail.as_view(), name='video-detail'),
]
