from django.db import models


class BankAccount(models.Model):
    owner = models.CharField(max_length=254)
    balance = models.IntegerField()
    type_card = models.CharField(max_length=20)
    currency_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.owner, self.pk, self.currency_type, self.balance}"
