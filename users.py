from bank import Bank
class User:
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_number = name+email
        self.account_type = account_type
        self.balance = 0
        self.history = []
        self.loan_taken = 0 

    def find_item_account(self,acc_number):
        for item in Bank.users:
            print(item.account_number)
            print(acc_number)
            if item.account_number.lower() == acc_number.lower():
                return item
        return None
    
    def transfer_balance(self,acc_number,amount):
        
        item = self.find_item_account(acc_number)
        if item:
            if self.balance > amount:
                item.balance += amount
                self.balance -= amount
                self.history.append(f'Transfer Balance in {acc_number} Amount is {amount}\n')
                print("Your Balance is Successfully Transfer \n")
            else:
                print("Transfer Amount Exceeded \n")
        else:
            print("Account Not Found \n")
        
        
    def create_account(self,customer):
        Bank.users.append(customer)

    def deposit(self,bank,amount):
        if(amount>0):
            self.balance +=amount
            bank.total_balance += amount
            print('Balance Added !')
            self.history.append(f'Add Balance {amount} \n')
        else:
            print('Sorry amount must be More then 1 \n') 

    def withdraw(self,bank,amount):
        if bank.is_bankrupt == False:
            if self.balance >= amount:
                self.balance -= amount
                bank.total_balance -= amount
                self.history.append(f'Withdraw Balance {amount} \n')
                print(f'Your withdrow money is {amount}\n')
                print('Thank you for using us\n')
            else:
                print('You do not have enough money\n')
        else:
            print("Sorry we are Bankrupt\n")
       
    
    

    def chack_balance(self):
        print(f'Your Balance is {self.balance}\n')

    def transaction_history(self):
        for item in self.history:
            print (item)


    def take_loan(self,bank,amount):
        if bank.is_bankrupt == False:
            if bank.loan_feature == True:
                if self.loan_taken <2:
                    self.balance +=amount
                    bank.total_loan_amounts += amount
                    bank.total_balance -= amount
                    self.loan_taken += 1
                    self.history.append(f'Take Loan {amount}\n')
                    print(f'You got loan,Your balance is {self.balance} \n')
                else:
                    print("You are not eligable for loan\n")
            else:
                print('Sorry This feature is currently unavailable\n')
        else:
            print('Sorry We are Bankrupt\n')

class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def add_new_customer(self, customer):
        Bank.users.append(customer)

    def delete_customer_account(self,bank,name):
        bank.delete_customer_account(name)

    def view_customer_list(self,bank):
        bank.view_customer_list()

    def bank_available_balance(self,bank):
        bank.total_balance_amount()

    def total_loan_amount(self,bank):
        bank.total_loan_amount()

    def bankrupt(self,bank,value):
        bank.bankrupt(value)
        
    



