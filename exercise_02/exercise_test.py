import unittest
from exercise_01.exercise import get_title

class TestExercise(unittest.TestCase):

    def test_get_test_table(self):
        url =""
        table_id = "example_table"
        result_csv_file = "result_csv.csv"
        expected_test_csv_file = "expected_test_csv.csv"

        result_csv = open(result_csv_file, 'r').read()
        expected_csv = open(expected_test_csv_file, 'r').read()

        get_table_and_save(url, table_id, result_csv_file)

        self.assertEqual(result_csv, expected_csv)

if __name__ == '__main__':
    unittest.main()