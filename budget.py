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
        if start > end:
            return 0
        b = self.get_all_budgets()

