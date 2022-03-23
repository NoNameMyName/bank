from random import randint

from bank.models import BankAccount


def transfer(sender, receiver, change):
    if sender.currency_type == receiver.currency_type:
        if sender.balance >= change:
            sender.balance = sender.balance - change
            receiver.balance = receiver.balance + change
        else:
            raise ValueError
    else:
        raise TypeError


def main():
    while True:
        sender = BankAccount.objects.get(id=randint(1, 10))
        receiver = BankAccount.objects.get(id=randint(1, 10))
        if sender.id != receiver.id:
            print(sender, receiver)
            break
    print(f"Balance before transfer\nSender:{sender.balance}\nReceiver:{receiver.balance}")
    print(f"Doing transfer")
    change = randint(0, 99999)
    transfer(
        sender=sender,
        receiver=receiver,
        change=change
    )
    print(f"Balance after transfer\nSender:{sender.balance}\nReceiver:{receiver.balance}")
    print(f"Accept")


main()

# from bank.utils.transfer_money import *
