from django.contrib.auth.models import User
from django.db import models


class BankAccount(models.Model):
    name = models.CharField(max_length=254)
    owner = models.ForeignKey(User, related_name='ow_accounts', on_delete=models.DO_NOTHING)
    balance = models.IntegerField(max_length=1000)


class OperationManager(models.Manager):
    def transfer_money(self, another):
        return sum(BankAccount.balance.self.pk, BankAccount.balance.another.pk)


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
    objects = OperationManager()
