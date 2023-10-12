from django.shortcuts import render
from rest_framework import viewsets
from api.models import MbotData
from api.serializers import MbotDataSerializer

# Create your views here.
class MbotDataViewSet(viewsets.ModelViewSet):
    queryset = MbotData.objects.all()
    serializer_class = MbotDataSerializer