from django.db import models


class BankAccount(models.Model):
    owner = models.CharField(max_length=254)
    balance = models.IntegerField()
    type_card = models.CharField(max_length=20)
    currency_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner, self.pk, self.currency_type, self.balance}"

    def is_balance_positive(self):
        return self.balance >= 0


class MoneyTransfer(models.Model):
    sender = models.ForeignKey(BankAccount, related_name='outcome_transfers', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(BankAccount, related_name='income_transfers', on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=255)
    change = models.IntegerField()
