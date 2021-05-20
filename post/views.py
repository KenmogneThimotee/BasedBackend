from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *



class ImageViewset(viewsets.ModelViewSet):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all()

class PostViewset(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all() 


class ClickForStyleViewset(viewsets.ModelViewSet):

    queryset = ClickForStyle.objects.all()
    serializer_class = ClickForStyleSerializer 

    def get_queryset(self):
        return ClickForStyle.objects.all()


class PostCommentViewset(viewsets.ModelViewSet):

    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer 

    def get_queryset(self):
        return PostComment.objects.all()


class UpVoteViewset(viewsets.ModelViewSet):

    queryset = UpVote.objects.all()
    serializer_class = UpVoteSerializer 

    def get_queryset(self):
        return UpVote.objects.all()


class DownVoteViewset(viewsets.ModelViewSet):

    queryset = DownVote.objects.all()
    serializer_class = DownVoteSerializer

    def get_queryset(self):
        return DownVote.objects.all()


class LikeCommentViewset(viewsets.ModelViewSet):

    queryset = LikeComment.objects.all()
    serializer_class = LikeCommentSerializer

    def get_queryset(self):
        return LikeComment.objects.all()


class DislikeCommentViewset(viewsets.ModelViewSet):

    queryset = DislikeComment.objects.all()
    serializer_class = DislikeCommentSerializer

    def get_queryset(self):
        return DislikeComment.objects.all()