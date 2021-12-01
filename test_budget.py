import unittest
from datetime import date

from .budget import BudgetService, Budget


class BudgetServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.b = BudgetService()

    def my_budgets(self):
        return self.fake_budgets

    def test_what(self):
        self.b.get_all_budgets = self.my_budgets
        self.fake_budgets = [Budget("202103", 31)]
        a = self.b.query(date(2021, 3, 1), date(2021, 3, 1))
        assert a == 31
        pass

if __name__ == "__main__":
    unittest.main()
