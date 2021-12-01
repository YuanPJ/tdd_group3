class Budget:
    def __init__(self, yearmonth, amount) -> None:
        self.year_month = yearmonth
        self.amount = amount

class BudgetService:
    def __init__(self):
        pass

    def get_all_budgets(self):
        pass

    def query(self, start, end):
        b = self.get_all_budgets()
        return b[0].amount
