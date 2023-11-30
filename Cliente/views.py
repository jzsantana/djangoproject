from django.shortcuts import render
from Cliente.models import  AccountCustomer, CreditCard, Transaction, SorteioUnico
import random
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
# from Cliente.serializers import TransactionSerializer

# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset =  Cliente.objects.all()
#     serializer_class = ClienteSerializer
           

class Transaction(APIView):
    ...
    
    
class CreateCreditCard(APIView):
    ...


class MakeLoan(APIView):
    def post(self, required):
        ...
    
    
