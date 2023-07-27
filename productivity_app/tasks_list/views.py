from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import List
from .models import ListItem

class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = List
        fields = ['name', 'description', 'date_created', 'date_updated']

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    parent_list = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = ListItem
        fields = ['name', 'description', 'date_created', 'date_updated']

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer



# Create your views here.
