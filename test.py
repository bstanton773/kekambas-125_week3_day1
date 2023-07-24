import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']),12)
    def test_two(self):
        self.assertEqual(solution(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']),10)
    def test_three(self):
        self.assertEqual(solution(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']),30)
    def test_empty(self):
        self.assertEqual(solution([]),0)

if __name__ == '__main__':
    unittest.main()