from random import randint

from faker import Faker

from bank.models import (
    BankAccount,
)

from bank.utils.constants import (
    FIRST_NAME_INDEX,
    TYPE_CARD,
    CURRENCY_TYPE,
)


def create_accounts(accounts_amount=10):
    fake = Faker()
    for _ in range(accounts_amount):
        name = fake.name().split()[FIRST_NAME_INDEX]
        type_of_card = TYPE_CARD[randint(0, 1)]
        currency_type = CURRENCY_TYPE[randint(0, 2)]
        money = randint(0, 99999999)
        BankAccount(owner=name, type_card=type_of_card, currency_type=currency_type, balance=money).save()


def main():
    print(f"DataBase before creation accounts: {BankAccount.objects.all()}")
    print("Create accounts")
    create_accounts()
    print(f"DataBase after creation accounts: {BankAccount.objects.all()}")


main()

# from bank.utils.fill_db import *
