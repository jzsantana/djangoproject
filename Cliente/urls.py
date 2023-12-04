from django.contrib import admin
from django.urls import path, include
from Cliente.viewset import AccountCustomerViewSet, DebitCardViewSet, CreditCardViewSet, TransactionViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.register('customer', CustomerViewSet)
router.register('account', AccountCustomerViewSet)
router.register('debit', DebitCardViewSet)
router.register('credit', CreditCardViewSet)
router.register('transaction', TransactionViewSet)
# router.register('extract', ExtractViewSet)


urlpatterns = [
    # path('transaction/', MakeTransaction.as_view(), name='make_transaction'),
    # path('transaction/<int:transaction_id>/', MakeTransaction.as_view(), name='get_detail'),
    # path('creditcard/', CreateCreditCard.as_view(), name='create_credit_card'),
]

