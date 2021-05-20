from .models import *
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.db import transaction
import datetime as dt
import json
from rest_framework import exceptions
from .models import *


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Image
        fields = "__all__"

            

class PostSerializer(serializers.ModelSerializer):

    images = serializers.ListField(child=serializers.FileField( max_length=100000,
    allow_empty_file=False,
    use_url=True ))


    class Meta:
        model = Post
        fields = "__all__"

    def create(self, **validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, **validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()

        image=validated_data.pop('images')
        for img in image:
            image =Image.objects.create(image=img,**validated_data)
            image.post = instance
            image.save()
        
        return instance

class ClickForStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClickForStyle
        fields = "__all__"


class PostCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostComment
        fields = "__all__"


class UpVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpVote
        fields = "__all__"

class DownVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = DownVote
        fields = "__all__"


class LikeCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeComment
        fields = "__all__"


class DislikeCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = DislikeComment
        fields = "__all__"