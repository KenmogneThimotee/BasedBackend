from django.shortcuts import render
from .stylization import SingleFactoryPredictor
from core.models import *
from rest_framework.response import Response

# Create your views here.


def predictOnTwoImage(request):

    user = request.user

    style = request.FILES['styleImage']
    target = request.FILES['targetImage']

    styleImage = StyleImage.objects.create(image=style,
    user=user,
    text_explanation=request.POST['text_style'],
    private=request.POST['private_style'])

    originalImage = OriginalImage.objects.create(image=target,
    user=user,
    text_explanation=request.POST['text_target'],
    private=request.POST['private_target'])

    styleImage.save()
    originalImage.save()

    predictor = SingleFactoryPredictor().get_instance()
    styledImage = predictor.predict(styleImage.image.path, originalImage.image.path)

    styledImage = StyledImage.objects.create(image=styledImage,
    user=user,
    styleImage=styleImage,
    originalImage=originalImage)

    styledImage.save()

    return Response({"eee":"eee"})



def predictOnOneImage(request):
    
    user = request.user

    style = request.FILES['styleImage']
    target = request.FILES['targetImage']

    styleImage = StyledImage.objects.get(id=request.POST['pk'])

    originalImage = OriginalImage.objects.create(image=target,
    user=user,
    text_explanation=request.POST['text_target'],
    private=request.POST['private_target'])

    styleImage.save()
    originalImage.save()

    predictor = SingleFactoryPredictor().get_instance()
    styledImage = predictor.predict(styleImage.image.path, originalImage.image.path)

    styledImage = StyledImage.objects.create(image=styledImage,
    user=user,
    styleImage=styleImage,
    originalImage=originalImage)

    styledImage.save()

    return Response({"eee":"eee"})



