from django.contrib import admin
from django.urls import path, include
from Cliente.viewset import AccountCustomerViewSet, DebitCardViewSet, CreditCardViewSet, TransactionViewSet, LoanViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('account', AccountCustomerViewSet)
router.register('debit', DebitCardViewSet)
router.register('credit', CreditCardViewSet)
router.register('transaction', TransactionViewSet)
router.register('loan', LoanViewSet)


urlpatterns = [
 
]

