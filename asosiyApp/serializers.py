from rest_framework import serializers
from .models import *

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class SuhbatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suhbat
        fields = "__all__"