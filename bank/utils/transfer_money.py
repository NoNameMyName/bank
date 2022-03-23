from random import randint

from bank.models import BankAccount


def transfer(sender, receiver, change):
    if sender.filter(currency_type="currency_type") == receiver.filter(currency_type="currency_type"):
        try:
            if sender.filter(balance="balance") >= change:
                sender.objects.balance = sender.objects.balance - change
                receiver.objects.balance = receiver.objects.balance + change
        except:
            raise ValueError
    else:
        raise TypeError


def main():
    while True:
        sender = BankAccount.objects.filter(id=randint(1, 10))
        receiver = BankAccount.objects.filter(id=randint(1, 10))
        print(sender, receiver)
        if sender.filter(id) != receiver.filter(id):
            break
    print(f"Balance before transfer\nSender:{sender.objects.balance}\nReceiver:{receiver.objects.balance}")
    print(f"Doing transfer")
    print(sender, receiver)
    change = randint(0, 99999)
    transfer(
        sender=sender.filter(balance=BankAccount.balance.get_lookup()),
        receiver=receiver.filter(balance=BankAccount.balance.get(id=5)),
        change=change
    )
    print(f"Accept")


main()

# from bank.utils.transfer_money import *
