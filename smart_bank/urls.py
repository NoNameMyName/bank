from django.urls import (
    path,
    include,
)

urlpatterns = [
    path('bank/api/', include("bank.urls")),
]
