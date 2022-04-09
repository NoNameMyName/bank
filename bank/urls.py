from django.urls import (
    path,
)

from bank.views import (
    api_bank_accounts,
    api_transfer_money
)

urlpatterns = [
    path('accounts/', api_bank_accounts),
    path('accounts/transfer_money/', api_transfer_money),
]
