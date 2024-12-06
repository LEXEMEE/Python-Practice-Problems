class ExpenseSplitter:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, person, amount):
        if person not in self.expenses:
            self.expenses[person] = 0.0
        self.expenses[person] += amount

    def calculate_balances(self):
        total_expense = sum(self.expenses.values())
        num_people = len(self.expenses)
        average_expense = total_expense / num_people

        balances = {person: amount - average_expense for person, amount in self.expenses.items()}
        return balances

    def settle_debts(self):
        balances = self.calculate_balances()
        creditors = [(person, amount) for person, amount in balances.items() if amount > 0]
        debtors = [(person, -amount) for person, amount in balances.items() if amount < 0]

        settlements = []
        creditors.sort(key=lambda x: x[1], reverse=True)
        debtors.sort(key=lambda x: x[1], reverse=True)

        while creditors and debtors:
            creditor, credit_amount = creditors.pop(0)
            debtor, debt_amount = debtors.pop(0)

            settle_amount = min(credit_amount, debt_amount)
            settlements.append((debtor, creditor, settle_amount))

            credit_remaining = credit_amount - settle_amount
            debt_remaining = debt_amount - settle_amount

            if credit_remaining > 0:
                creditors.insert(0, (creditor, credit_remaining))
            if debt_remaining > 0:
                debtors.insert(0, (debtor, debt_remaining))

        return settlements


# Example Usage
if __name__ == "__main__":
    splitter = ExpenseSplitter()
    
    # Adding expenses
    splitter.add_expense("Alice", 120)
    splitter.add_expense("Bob", 80)
    splitter.add_expense("Charlie", 100)
    
    # Calculate and display balances
    print("Balances:")
    balances = splitter.calculate_balances()
    for person, balance in balances.items():
        print(f"{person}: {'Owes' if balance < 0 else 'Is Owed'} {abs(balance):.2f}")

    # Display settlements
    print("\nSettlements:")
    settlements = splitter.settle_debts()
    for debtor, creditor, amount in settlements:
        print(f"{debtor} pays {creditor} {amount:.2f}")
