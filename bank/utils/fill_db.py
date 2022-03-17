from random import getrandbits

from faker import Faker

from bank.models import (
    BankAccount
)

from bank.utils.constants import (
    FIRST_NAME_INDEX
)


def create_accounts(accounts_amount=10):
    fake = Faker()
    nicknames = set()
    for _ in range(accounts_amount):
        name = fake.name().split()[FIRST_NAME_INDEX]
        nicknames.add(name)
    accounts = [BankAccount(name=name) for name in nicknames]
    BankAccount.objects.bulk_create(accounts)


def main():
    print("Create accounts")
    create_accounts()


main()
