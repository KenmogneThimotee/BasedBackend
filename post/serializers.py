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

class ClickForStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClickForStyle
        fields = "__all__"


class PostCommentSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=CustumUser)
    #response = super().__init__(many=True)

    class Meta:
        model = PostComment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    image = ImageSerializer(many=True)
    cickForStyle = ClickForStyleSerializer(many=True)
    comment = PostCommentSerializer(many=True)


    class Meta:
        model = Post
        fields = "__all__"

    def create(self, **validated_data):
        return Post.objects.create(**validated_data)

    """
    def update(self, instance, **validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()

        image=validated_data.pop('images')
        for img in image:
            image =Image.objects.create(image=img,**validated_data)
            image.post = instance
            image.save()
        
        return instance
    """



class UpVoteSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=CustumUser)
    post = serializers.PrimaryKeyRelatedField(queryset=Post)

    class Meta:
        model = UpVote
        fields = "__all__"



class DownVoteSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=CustumUser)
    post = serializers.PrimaryKeyRelatedField(queryset=Post)

    class Meta:
        model = DownVote
        fields = "__all__"


class LikeCommentSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=CustumUser)
    post = serializers.PrimaryKeyRelatedField(queryset=PostComment)

    class Meta:
        model = LikeComment
        fields = "__all__"


class DislikeCommentSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=CustumUser)
    post = serializers.PrimaryKeyRelatedField(queryset=PostComment)

    class Meta:
        model = DislikeComment
        fields = "__all__"