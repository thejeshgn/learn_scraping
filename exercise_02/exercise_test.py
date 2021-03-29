import os
import unittest
from exercise_02.exercise import get_table_and_save

class TestExercise(unittest.TestCase):

    def test_get_test_table(self):
        url ="https://thejeshgn.github.io/learn_scraping/table1.html"
        table_id = "example_table"
        result_csv_file = os.path.join(os.path.dirname(__file__), "result_csv.csv")
        expected_test_csv_file = os.path.join(os.path.dirname(__file__),"expected_test_csv.csv")

        result_csv = open(result_csv_file, 'r').read()
        expected_csv = open(expected_test_csv_file, 'r').read()

        get_table_and_save(url, table_id, result_csv_file)

        os.remove(result_csv)
        self.assertEqual(result_csv, expected_csv)

    def test_get_district_table(self):
        url ="https://thejeshgn.github.io/learn_scraping/table1.html"
        table_id = "districts_in_India"
        result_csv_file = os.path.join(os.path.dirname(__file__),"district_result_csv.csv")
        expected_test_csv_file = os.path.join(os.path.dirname(__file__),"district_expected_test_csv.csv")

        result_csv = open(result_csv_file, 'r').read()
        expected_csv = open(expected_test_csv_file, 'r').read()

        get_table_and_save(url, table_id, result_csv_file)

        os.remove(result_csv)
        self.assertEqual(result_csv, expected_csv)


if __name__ == '__main__':
    unittest.main()