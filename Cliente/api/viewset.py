from rest_framework.viewsets import ModelViewSet
# from rest_framework import serializers
from Cliente import models
from rest_framework import filters
from Cliente.api.serializers import ClienteSerializer
# # from django_filters.rest_framework import DjangoFilterBackend


class ClienteViewSet(ModelViewSet):
    queryset =  models.Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'id']