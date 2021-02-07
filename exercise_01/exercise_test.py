import unittest
from exercise_01.exercise import get_title

class TestExercise(unittest.TestCase):

    def test_get_google(self):
        answer = "Google"
        url = "https://www.google.com/"
        test_answer = get_title(url)
        self.assertTrue(test_answer==answer, "The test_answer doens't have the correct answer")

    def test_english_wikipedia(self):
        answer = "Wikipedia, the free encyclopedia"
        url = "https://en.wikipedia.org/wiki/Main_Page"
        test_answer = get_title(url)
        self.assertTrue(test_answer==answer, "The test_answer doens't have the correct answer")

if __name__ == '__main__':
    unittest.main()