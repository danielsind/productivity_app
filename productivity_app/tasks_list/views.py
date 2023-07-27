from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import List

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['name', 'description', 'date_created', 'date_updated']

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer



# Create your views here.
