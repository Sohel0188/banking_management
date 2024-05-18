
from bank import Bank
from users import Admin
from users import Customer

Amar_bank = Bank('Amar Bank')
def register():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    address = input('Enter Your Address : ')
    print("1 : Current Account\n2 : Savings Account")
    account_type = int(input())
    account = "current" if account_type == 1 else "savings"

    customer = Customer(name, email, address, account)
    customer.create_account(customer)
    print("Account created successfully!")
    user_menu(customer)

def login():
    print("Enter User Name: ")
    user_name = input()
    print("Enter User Password (Email): ")
    user_password = input()
    
    for customer in Bank.users:
        if customer.name == user_name and customer.email == user_password:
            print("Login successful!")
            user_menu(customer)
            return
    print("Invalid account")

def user_menu(customer):
    while True:
        print(f"Welcome {customer.name}!!")
        print("1. Deposit Balance  ")
        print("2. Withdraw Balance  ")
        print("3. Check Balance  ")
        print("4. Account History  ")
        print("5. Take Loan  ")
        print("6. Transfer Banalce  ")
        print("7. Exit ")

        choice = int(input("Enter Any Nubmer : "))
        if choice == 1:
            balance = int(input("Enter Your Deposit Amount : "))
            customer.deposit(Amar_bank,balance)
        elif choice == 2:
            amount = int(input('Enter Yout Withdraw Amount : '))
            customer.withdraw(Amar_bank,amount)
        elif choice == 3:
            customer.chack_balance()
        elif choice == 4:
            customer.transaction_history()
        elif choice == 5:
            loan_amount = int(input('Enter Your Loan Amount : '))
            customer.take_loan(Amar_bank,loan_amount)
        elif choice == 6:
            acc_num = input("Enter Account Number : ")
            tr_amount = int(input("Enter Transfer Amount : "))
            customer.transfer_balance(acc_num,tr_amount)
        elif choice == 7:
            break
        else:
            print('Invalid Input')

def admin_menu():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    address = input('Enter Your Address : ')
    
    admin = Admin(name,email,address)

    while(True):
        print(f"Welcome {admin.name}!!")
        print("1. Add New Account  ")
        print("2. Delete Account ")
        print("3. See All User Accounts List  ")
        print("4. Total Available Balance Of The Bank ")
        print("5. Total Loan Amount  ")
        print("6. On or Off The Loan Feature")
        print("7. On or Off The Bankrupt Feature  ")
        print("8. Exit ")
        choice = int(input("Enter Any Nubmer : "))
        if choice == 1:
            name = input('Enter Your Name :')
            email = input('Enter Your Email :')
            address = input('Enter Your Address :')
            print("1 : Current Account\n2 : Savings Account")
            account_type = int(input())
            print(account_type)
            if(account_type ==1):
                account = "Current"
            elif(account_type == 2):
                account = "Savings"
            customer = Customer(name,email,address,account)
            admin.add_new_customer(customer)
        elif choice == 2:
            name = input("Enter The Name Of User : ")
            admin.delete_customer_account(Amar_bank,name)

        elif choice == 3:
            admin.view_customer_list(Amar_bank)
        elif choice == 4:
            admin.bank_available_balance(Amar_bank)
        elif choice == 5:
            admin.total_loan_amount(Amar_bank)
        elif choice == 6:
            print('1 : Loan Feature On \n0 : Loan Feature Off')
            value = int(input('Enter Value : '))
            admin.loan_feature(Amar_bank,value)
        elif choice == 7:
            print('1 : Active Bank \n0 : Bankrupt')
            option = int(input())
            admin.bankrupt(Amar_bank,option)
        elif choice == 8:
            break
        else:
            print('Invalid Input')
while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("1 : Login \n2 : Register ")
        value = int(input())

        if value == 1:
            login()
        elif value == 2:
            register()
        else:
            print('Invalid Input')
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")
