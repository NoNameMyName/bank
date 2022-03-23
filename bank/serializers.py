from rest_framework import serializers

from bank.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ("owner", "balance", "type_card", "currency_type",)