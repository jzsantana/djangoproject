from django.contrib import admin
from django.urls import path
from .views import TudoAPIView

urlpatterns = [
    path('criarcartao', views.criar_cartao_credito, name='criar_cartao_credito'),
    path('all', TudoAPIView.as_view, name='all'),
    # path('api/', include(route.urls))
]

