from django.db import models


class BankAccount(models.Model):
    owner = models.CharField(max_length=254)
    balance = models.IntegerField(max_length=1000)
    type_card = models.CharField(max_length=20)
    currency_type = models.CharField(max_length=50)


class MoneyTransfer(models.Model):
    sender = models.ForeignKey(
        "BankAccount",
        related_name='outcome_transfers',
        on_delete=models.DO_NOTHING
    )
    receiver = models.ForeignKey(
        "BankAccount",
        related_name='income_transfers',
        on_delete=models.DO_NOTHING
    )
    comment = models.CharField(max_length=255)
    time_now = models.TimeField(auto_now=True)
