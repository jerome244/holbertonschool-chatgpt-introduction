class Checkbook:
    # Class Description:
    # This class simulates a simple checkbook with deposit, withdrawal, and balance retrieval functionalities.
    # It keeps track of the current balance and performs operations based on user input.

    def __init__(self):
        # Initializes a new checkbook with a starting balance of 0.0.
        self.balance = 0.0

    def deposit(self, amount):
        # Method Description:
        # This method accepts a deposit amount and adds it to the current balance.
        # It then prints the deposited amount and the updated balance.
        
        # Parameters:
        # amount (float): The amount to be deposited into the account.
        
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Method Description:
        # This method accepts a withdrawal amount and subtracts it from the current balance,
        # if there are sufficient funds. If the balance is insufficient, an error message is shown.
        
        # Parameters:
        # amount (float): The amount to be withdrawn from the account.
        
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Method Description:
        # This method prints the current balance of the checkbook.
        
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Main Function:
    # This is the main entry point of the program. It continuously asks the user what operation they'd like to perform
    # (deposit, withdraw, check balance, or exit). Based on the user's input, it calls the corresponding method
    # from the Checkbook class.
    
    cb = Checkbook()  # Create a new checkbook instance.
    
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'.
        
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value for deposit.")
        
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value for withdrawal.")
        
        elif action.lower() == 'balance':
            cb.get_balance()
        
        else:
            print("Invalid command. Please try again.")  # Inform the user if they enter an invalid action.

if __name__ == "__main__":
    main()
