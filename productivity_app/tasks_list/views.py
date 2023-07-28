from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import List
from .models import ListItem
from django.contrib.auth import get_user_model

class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.all())
    class Meta:
        model = List
        fields = ['user','name', 'description', 'date_created', 'date_updated']

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    parent_list = serializers.PrimaryKeyRelatedField(queryset = List.objects.all())
    class Meta:
        model = ListItem
        fields = ['name', 'description', 'date_created', 'date_updated','parent_list']

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer



# Create your views here.
