from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from bank.models import BankAccount

from bank.utils.transfer_money import transfer

from bank.serializers import (
    BankAccountSerializer,
    TransferMoneySerializer
)


@api_view(["GET", "POST"])
def api_bank_accounts(request):
    if request.method == "GET":
        accounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def api_transfer_money(request):
    if request.method == "POST":
        serializer = TransferMoneySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            print(f"New transfer: {serializer.transfer(request)}")
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        print(f"serializers errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
