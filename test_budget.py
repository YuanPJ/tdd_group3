import unittest
from datetime import date

from budget import Budget, BudgetService



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
    
    def test_one_day_only(self):
        self.fake_budgets = [Budget("202103",31)]
        self.b.get_all_budgets = self.my_budgets
        result = self.b.query(date(2021, 3, 1), date(2021, 3, 1))
        self.assertEqual(1.0, result)
    
    def test_multiply_day_in_same_month(self):
        self.fake_budgets = [Budget("202103",31), Budget("202104", 300)]
        self.b.get_all_budgets = self.my_budgets
        result = self.b.query(date(2021, 3, 1), date(2021, 3, 6))
        self.assertEqual(6.0, result)
    
    def test_multiply_day_in_one_month(self):
        self.fake_budgets = [Budget("202103",31), Budget("202104", 300)]
        self.b.get_all_budgets = self.my_budgets
        result = self.b.query(date(2021, 3, 1), date(2021, 3, 31))
        self.assertEqual(31.0, result)
    
    def test_multiply_day_in_diff_month(self):
        self.fake_budgets = [Budget("202103",31), Budget("202104", 300)]
        self.b.get_all_budgets = self.my_budgets
        result = self.b.query(date(2021, 3, 30), date(2021, 4, 3))
        self.assertEqual(32.0, result)

    def test_multiply_day_in_multiple_month(self):
        self.fake_budgets = [Budget("202103",31), Budget("202104", 300), Budget("202106", 6000)]
        self.b.get_all_budgets = self.my_budgets
        result = self.b.query(date(2021, 3, 30), date(2021, 6, 7))
        self.assertEqual(1702.0, result)

    def test_multiply_day_in_cross_year(self):
        self.fake_budgets = [Budget("202103",31), Budget("202104", 300), Budget("202204", 6000)]
        self.b.get_all_budgets = self.my_budgets
        result = self.b.query(date(2021, 3, 30), date(2022, 4, 7))
        self.assertEqual(1702.0, result)


if __name__ == "__main__":
    unittest.main()
