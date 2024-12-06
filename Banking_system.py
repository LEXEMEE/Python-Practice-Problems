class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        return f"{amount} deposited. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"{amount} withdrawn. Current balance: {self.balance}"

    def get_balance(self):
        return f"Account Balance: {self.balance}"

    def get_account_details(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            return "Account number already exists."
        self.accounts[account_number] = BankAccount(account_number, account_holder, initial_balance)
        return f"Account created for {account_holder} with Account Number: {account_number}."

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def perform_transaction(self, account_number, transaction_type, amount=0):
        account = self.get_account(account_number)
        if not account:
            return "Account not found."

        if transaction_type == "deposit":
            return account.deposit(amount)
        elif transaction_type == "withdraw":
            return account.withdraw(amount)
        else:
            return "Invalid transaction type. Use 'deposit' or 'withdraw'."

    def view_account_details(self, account_number):
        account = self.get_account(account_number)
        if not account:
            return "Account not found."
        return account.get_account_details()


# Example Usage
if __name__ == "__main__":
    bank = BankingSystem()

    # Create Accounts
    print(bank.create_account("1001", "Alice", 500))
    print(bank.create_account("1002", "Bob", 1000))

    # Deposit and Withdrawals
    print(bank.perform_transaction("1001", "deposit", 300))
    print(bank.perform_transaction("1002", "withdraw", 200))

    # Balance Inquiries
    account1 = bank.get_account("1001")
    account2 = bank.get_account("1002")
    if account1:
        print(account1.get_balance())
    if account2:
        print(account2.get_balance())

    # View Account Details
    print(bank.view_account_details("1001"))
    print(bank.view_account_details("1002"))
