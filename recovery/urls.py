from . import views
from django.contrib import admin
from django.urls import path, include, re_path
from . views import  submit_recovery_request, wallet_recovery_view, blockchain_transaction_view, contact_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('submit-recovery/', views.submit_recovery_request, name='submit_recovery_request'),
    path('wallet-recovery/', views.wallet_recovery_view, name='wallet_recovery_view'),
    path('blockchain-transaction/', views.blockchain_transaction_view, name='blockchain_transaction_view'),
    path('contact/', views.contact_view, name='contact_view'),
]
