import unittest
from datetime import date

from budget import BudgetService



class BudgetServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.b = BudgetService()

    def my_budgets(self):
        return self.fake_budgets

    def test_invalid_start_end(self):
        result = self.b.query(date(2021, 3, 3), date(2021, 3, 1))
        self.assertEqual(0, result)


    def test_db_no_data(self):
        self.fake_budgets = []
        self.b.get_all_budgets = self.my_budgets
        result = self.b.query(date(2021, 3, 1), date(2021, 3, 1))
        self.assertEqual(0, result)

if __name__ == "__main__":
    unittest.main()
