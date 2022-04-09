from rest_framework import serializers

from bank.models import (
    BankAccount,
    MoneyTransfer,
)


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ("owner", "balance", "type_card", "currency_type")


class TransferMoneySerializer(serializers.ModelSerializer):

    class Meta:
        model = MoneyTransfer
        fields = ("sender", "receiver", "comment", "change")

    def validate(self, data):
        print(f"DATA Before validate: {data}")
        print(f"DATA Before validate: {data.get('sender')}")
        if data.get('sender') > data.get("change"):
            print("Sorry, you don`t have enough money")
            return serializers.ErrorDetail("Not enough money or not correct request")
        validated_data = super().validate(data)
        print(f"DATA After validate: {validated_data}")
        return validated_data

    # json > python data
    def to_internal_view(self, data):
        internal_data = super().to_internal_value(data)
        return internal_data


    def transfer(self, data):
        pass


    # python model > Json
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

# serializers.ValidationError("error" : "")
