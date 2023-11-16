# from rest_framework import viewsets
# from rest_framework import filters
# # from django_filters.rest_framework import DjangoFilterBackend


# class ClienteViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.ClienteSerializer
#     queryset = models.Cliente.objects.all()

#     # filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['nome', 'telefone', 'email']

#     filter_backends = [filters.SearchFilter]
#     search_fields = ['nome', 'telefone', 'email', '']