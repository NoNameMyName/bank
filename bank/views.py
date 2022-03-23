from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from bank.models import BankAccount

from bank.serializers import BankAccountSerializer


@api_view(["GET", "POST"])
def api_bank_accounts(request):
    if request.method == "GET":
        accounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(accounts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BankAccountSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
