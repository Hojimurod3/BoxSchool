from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import TeacherSerializer, PostSerializer, VideoSerializer
from .models import Video, Teacher, Post


class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherPostsList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['pk']
        return Post.objects.filter(teacher_id=teacher_id)

    def post(self, request, *args, **kwargs):
        request.data['teacher'] = kwargs['pk']
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherVideosList(generics.ListCreateAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['pk']
        return Video.objects.filter(teacher_id=teacher_id)

    def post(self, request, *args, **kwargs):
        request.data['teacher'] = kwargs['pk']
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class VideoListCreate(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
