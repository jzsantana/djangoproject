from django.contrib import admin
from django.urls import path
# from Cliente.api.viewset import *
from Cliente.viewset import CustomerViewSet, AccountCustomerViewSet, CustomerViewSet
from rest_framework.routers import SimpleRouter
# from .views import TudoAPIView

router = SimpleRouter()
router.register('account', AccountCustomerViewSet)
router.register('customer', CustomerViewSet)


# urlpatterns = [
    
#     # path('clientes/', ClienteViewSet.as_view), 
#     # path('criarcartao', views.criar_cartao_credito, name='criar_cartao_credito'),
#     # path('all', TudoAPIView.as_view, name='all'),
#     # path('api/', include(route.urls))
# ]

