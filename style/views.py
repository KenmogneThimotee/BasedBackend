from django.shortcuts import render
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
from core.models import *
from rest_framework.response import Response

# Create your views here.

predictor_instance = None


class Predictor():
    
    def __init__(self):

        self.hub_module = hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')


    def prepareImage(self, file_path):

        content_image = plt.imread(file_path)
        content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.

        return content_image


    def prepareStyleImage(self, file_path):

        style_image = plt.imread(file_path)
        style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.

        style_image = tf.image.resize(style_image, (256, 256))
        
        return style_image

    def predict(self, styleImage_path, contentImage_path):

        content_image = self.prepareImage(contentImage_path)
        style_image = self.prepareStyleImage(styleImage_path)

        outputs = self.hub_module(tf.constant(content_image), tf.constant(style_image))
        stylized_image = outputs[0]

        return style_image


class SingleFactoryPredictor():
    
    def __init__():
        if predictor_instance:
            return predictor_instance
        else:
            predictor_instance = Predictor()
            return predictor_instance


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

    predictor = SingleFactoryPredictor()
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

    predictor = SingleFactoryPredictor()
    styledImage = predictor.predict(styleImage.image.path, originalImage.image.path)

    styledImage = StyledImage.objects.create(image=styledImage,
    user=user,
    styleImage=styleImage,
    originalImage=originalImage)

    styledImage.save()

    return Response({"eee":"eee"})



