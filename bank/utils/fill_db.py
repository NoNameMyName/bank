from random import randint

from faker import Faker

from bank.models import (
    BankAccount,
)

from bank.utils.constants import (
    FIRST_NAME_INDEX,
    TYPE_CARD,
    CURRENCY_TYPE,
    MONEY,
)


def create_accounts(accounts_amount=10):
    fake = Faker()
    for _ in range(accounts_amount):
        name = fake.name().split()[FIRST_NAME_INDEX]
        type_of_card = TYPE_CARD[randint(0, 1)]
        currency_type = CURRENCY_TYPE[randint(0, 2)]
        money = MONEY
        accounts = BankAccount(owner=name, type_card=type_of_card, currency_type=currency_type, balance=money)
    BankAccount.objects.bulk_create(accounts)


def main():
    print("Create accounts")
    create_accounts()


main()
