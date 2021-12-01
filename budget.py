import calendar
from datetime import timedelta
from typing import Collection
from collections import Counter 
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

        load_days = []
        start_date = start
        end_date = end
        shift_time = timedelta(days=1)
        while start_date <= end_date:
            load_days.append(start_date.strftime("%Y%m"))
            start_date = start_date + shift_time
        
        count = Counter(load_days)

        # year_month_of_start = start.strftime("%Y%m")
        budget_of_start_month = 0
        total = 0
        for year_month in count:
            for budget in b:
                if budget.year_month == year_month:
                    budget_of_month = budget.amount
                    month_day_num = calendar.monthrange(int(year_month[:4]), int(year_month[4:]))[1]
                    total += budget_of_month / month_day_num * count[year_month]
        # start_month_day_num = calendar.monthrange(start.year, start.month)[1]
        
    
        return total