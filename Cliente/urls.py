from django.contrib import admin
from django.urls import path, include
# from Cliente.api.viewset import *
from Cliente.viewset import AccountCustomerViewSet, DebitCardViewSet, CreditCardViewSet
from rest_framework.routers import SimpleRouter
# from .views import TudoAPIView

router = SimpleRouter()
router.register('account', AccountCustomerViewSet)
router.register('debit', DebitCardViewSet)
router.register('credit', CreditCardViewSet)
