from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *



class CustumUserViewset(viewsets.ModelViewSet):

    queryset = CustumUser.objects.all()
    serializer_class = CustumUserSerializer

    def get_queryset(self):
        return CustumUser.objects.all()


class StyledImageViewset(viewsets.ModelViewSet):

    queryset = StyledImage.objects.all()
    serializer_class = StyledImageSerializer

    def get_queryset(self):
        return StyledImage.objects.all()



class StyleImageViewset(viewsets.ModelViewSet):

    queryset = StyleImage.objects.all()
    serializer_class = StyleImageSerializer

    def get_queryset(self):
        return StyleImage.objects.all()


class StyledImageCollectionViewset(viewsets.ModelViewSet):

    queryset = StyledImageCollection.objects.all()
    serializer_class = StyledImageCollectionSerializer

    def get_queryset(self):
        return StyledImageCollection.objects.all()


class StyleImageCollectionViewset(viewsets.ModelViewSet):

    queryset = StyleImageCollection.objects.all()
    serializer_class = StyleImageCollectionSerializer

    def get_queryset(self):
        return StyleImageCollection.objects.all()