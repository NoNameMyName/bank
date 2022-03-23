from django.urls import (
    path,
)

from bank.views import api_bank_accounts

urlpatterns = [
    path('accounts/', api_bank_accounts),
]
