from abc import ABCMeta, abstractmethod
import random
import sys

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):
    
    def __init__(self) -> None:
        self.savingsAccount = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = random.randint(10000, 99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print(f"Your account creation is successful. Your account number is {self.accountNumber}")

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication is successful")
                self.accountNumber = accountNumber
                return True
            else:
                print('Authentication is failed')
                return False
        else:
            print('Authentication is failed')
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print('Insufficent Balance')
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            print(f"Withdrawal was successful.")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print(f"Deposit was successful.")
        self.displayBalance()

    def displayBalance(self):
        print(f"Available Balance: {self.savingsAccount[self.accountNumber][1]}")


savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exist")
    userChoice = int(input())

    if userChoice == 1:
        name = input('Enter your name: ')
        deposit = int(input('Enter your initial deposit: '))
        savingsAccount.createAccount(name, deposit)

    elif userChoice == 2:
        name = input('Enter your name: ')
        accountNumber = int(input('Enter your account number: '))
        authentication_staus = savingsAccount.authenticate(name, accountNumber)
        if authentication_staus:
            while True:
                print('Enter 1 to withdraw')
                print('Enter 2 to deposit')
                print('Enter 3 to display available balance')
                print('Enter 4 to go back to previous menu')
                print('Enter 5 to exist')
                userChoice = int(input())
                if userChoice == 1:
                   withdrawalAmount = int(input('Enter the withdrawal amount: '))
                   savingsAccount.withdraw(withdrawalAmount)
                elif userChoice == 2:
                    deposit_Amount = int(input('Enter the Deposit amount: '))
                    savingsAccount.deposit(deposit_Amount)
                elif userChoice == 3:
                    savingsAccount.displayBalance()
                elif userChoice == 4:
                    break
                elif userChoice == 5:
                    sys.exit('Logging you out')
    elif userChoice == 3:
        sys.exit('Logging you out.. Bye')