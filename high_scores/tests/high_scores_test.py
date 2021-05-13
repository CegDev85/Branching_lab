
import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [5,2,8,21,10,6]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(6, latest(self.scores)) #this is me checking the result is 6, from the scores list, when i use the function in high_scores.py

    # Test personal best (the highest score in the list)
    def test_higest_score_in_list(self):
        self.assertEqual(21 ,highest_score(self.scores)) #i created this function in the high scores.py,and it wasnt importing in, import * means all i add are imported now

    # Test top three from list of scores
    def test_top_three_from_list(self):
        self.assertEqual([21,10,8], top_three(self.scores))

    # Test ordered from highest tp lowest
    def test_ordered_from_highest_to_lowest(self):
        self.assertEqual([21,10,8,6,5,2], highest_to_lowest(self.scores))

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
