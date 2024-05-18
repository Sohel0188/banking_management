class Bank:
    users = []
    def __init__(self,bank_name) -> None:
        self.bank_name = bank_name
        self.is_bankrupt = False
        self.loan_feature = True
        self.total_loan_amounts = 0
        self.total_balance = 10000

    def bankrupt(self,value):
        if value == 0:
            self.is_bankrupt = True
        elif value == 1:
            self.is_bankrupt = False

    def find_item(self, name):
        for item in self.users:
            if item.name.lower() == name.lower():
                return item
        return None
    
    def delete_customer_account(self, name):
        item = self.find_item(name)
        if item:
            self.users.remove(item)
            print("Customer deleted\n")
        else:
            print("Customer not found\n")

    def view_customer_list(self):
        print("Our Customer List\n")
        print("Name \t Email \t Address\t Account Number")
        for item in Bank.users:
            print(f"{item.name}\t{item.email}\t{item.address}\t{item.account_number}")
            

    def total_loan_amount(self):
        print(f'Total Loan Amount : {self.total_loan_amounts}\n')
    
    def total_balance_amount(self):
        print(f'Bank Total Balance is {self.total_balance}\n')

    def loan_features(self,value):
        if value == 0:
            self.loan_feature = False
            print('Loan feature is off now \n')
        elif value == 1:
            self.loan_feature = True
            print('Loan feature is active now')
    
   
