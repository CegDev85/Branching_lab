import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [5,2,8,21,10,6]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(6, latest(self.scores)) #this is me checking the result is 6, from the scores list, when i use the function in high_scores.py
    # Test personal best (the highest score in the list)


    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
