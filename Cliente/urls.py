from django.contrib import admin
from django.urls import path, include
# from Cliente.api.viewset import *
from Cliente.viewset import AccountCustomerViewSet
from rest_framework.routers import SimpleRouter
# from .views import TudoAPIView

router = SimpleRouter()
router.register('account', AccountCustomerViewSet)
# router.register('customer', CustomerViewSet)


urlpatterns = [
      
]

