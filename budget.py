import calendar
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

        year_month_of_start = start.strftime("%Y%m")
        budget_of_start_month = 0
        for budget in b:
            if budget.year_month == year_month_of_start:
                budget_of_start_month = budget.amount
        else:
            budget_of_start_month = 0
        start_month_day_num = calendar.monthrange(start.year, start.month)[1]
        return budget_of_start_month / start_month_day_num