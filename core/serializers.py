from .models import *
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.db import transaction
import datetime as dt
import json
from rest_framework import exceptions
from .models import *


class CustumUserSerializer(serializers.ModelSerializer):

    class Meta:
        model =  CustumUser
        fields = "__all__"


class StyledImageCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model =  StyledImageCollection
        fields = "__all__"


class StyleImageCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model =  StyleImageCollection
        fields = "__all__"


class StyleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model =  StyleImage
        fields = "__all__"


class StyledImageSerializer(serializers.ModelSerializer):

    class Meta:
        model =  StyledImage
        fields = "__all__"

