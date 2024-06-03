class Account:
    def __init__(self,account_number,pin):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = 0
        self.is_frozen = False
        self.deposit_history = []  # Initialize empty lists for deposits and withdrawals
        self.withdraw_history = []
        self.accounts_lists = []

    def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "wrong pin"  

    def deposit(self,pin, amount_deposited):
        if pin == self.__pin:
           self.__balance += amount_deposited
           self.deposit_history.append(amount_deposited)
           return "Deposit successful!"
        else:
          return "Wrong pin"
  

def withdraw(self, pin, amount_withdrawn):
    if pin == self.__pin:
        if amount_withdrawn <= self.__balance:
            self.__balance -= amount_withdrawn
            self.withdraw_history.append(amount_withdrawn)
            return f"Withdrawal of ${amount_withdrawn:.2f} successful. New balance: ${self.__balance:.2f}"

        else:
            return "Insufficient funds"
    else:
        return "Wrong pin"

          
def view_account_details(self, pin):
    if pin == self.__pin:
        return f"Your account number is {self.account_number} and current balance is ${self.__balance:.2f}"
    else:
        return "Wrong pin"



def update_account_ownership(self,pin,account_number,new_pin):
    if pin == self.__pin:
        if pin != new_pin:
            return f"succefully updated the owner's information"
        else: 
            return f"please put another different pin"
    else:
        return "wrong pin"     


def account_statement(self, pin):
    if pin == self.__pin:
        return f"Your account number is {self.account_number} and current balance is ${self.__balance:.2f}"
    else:
        return "Wrong pin"

def set_overdraft_limit(self, pin, amount_withdrawn):
    if pin == self.pin:
        if amount_withdrawn <= 250000:
            return f"You have successfully withdrawn {amount_withdrawn}"
        else:
            return "You can only withdraw money below 250,000"
    else:
        return "Wrong pin"
    
def calculate_interest(self, pin, balance, rate):
    if pin == self.__pin:
        interest = (balance * rate) / 100
        return f"Your interest rate is {interest:.2f}"  # Format the interest as a floating-point number with 2 decimal places
    else:
        return "Wrong pin" 


def freeze_account(self):
        if not self.is_frozen:
            self.is_frozen = True
            return "Account frozen successfully."
        else:
            return "Account is already frozen."

def unfreeze_account(self):
        if self.is_frozen:
            self.is_frozen = False
            return "Account unfrozen."
        else:
            return "Account is not frozen."
            

def history_transaction(self,pin):
    if pin == self.__pin:
        print("Deposits:", self.deposit_history)
        print("Withdrawals:", self.withdraw_history)


def minimum_balance(self,pin):
    if pin == self.__pin:
        if self.__balance <= 50:
            return "You have reached your minimum balance"
        else:
            return "you have not reached your minimum balance"  
    else:
        return "wrong pin"          



def transaction_funds(self,pin,account_transfering_to,amount_transfered):
    if pin == self.__pin:
        return f"This {amount_transfered} has been tranfered to {account_transfering_to} account"
    else:
        return "wrong pin"  




def cleanUp(self, pin, account_transfer):
        if pin == self.__pin:
            return f"Your account balance of {self.__balance} has been successfully transferred to {account_transfer} account"
        else:
            return "Wrong pin"

def close_account(self, pin, account_number):
        if pin == self.__pin:
            for account in self.accounts_lists:
                if account_number == account.account_number:  # Assuming account has an attribute 'account_number'
                    self.accounts_lists.remove(account)
                    return f"This {account_number} account has been successfully removed"
            return "The account number does not exist in the accounts list"
        else:
            return "Wrong pin"

                   
        


