from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class TopicModelViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class SuhbatModelViewSet(ModelViewSet):
    queryset = Suhbat.objects.all()
    serializer_class = SuhbatSerializer