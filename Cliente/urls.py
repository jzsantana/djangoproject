from django.contrib import admin
from django.urls import path, include
# from Cliente.api.viewset import *
from Cliente.viewset import AccountCustomerViewSet, DebitCardViewSet, CreditCardViewSet, TransactionViewSet
from rest_framework.routers import SimpleRouter
from Cliente.views import MakeTransaction, CreateCreditCard
# from .views import TudoAPIView

router = SimpleRouter()
# router.register('customer', CustomerViewSet)
router.register('account', AccountCustomerViewSet)
router.register('debit', DebitCardViewSet)
router.register('credit', CreditCardViewSet)
# router.register('transaction', TransactionViewSet)

urlpatterns = [
    path('transaction/', MakeTransaction.as_view(), name='make_transaction'),
    # path('transaction/<int:transaction_id>/', MakeTransaction.as_view(), name='get_detail'),
    path('creditcard/', CreateCreditCard.as_view(), name='create_credit_card'),
]

