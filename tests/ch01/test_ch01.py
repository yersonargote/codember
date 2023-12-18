"""
keys house HOUSE house keys -> keys2house3
cup te a cup -> cup2te1a1
houses house housess -> houses1house1housess1
"""
import unittest
from tests.utils.files import read_file
from ch01.solution import solve


class TestCh01(unittest.TestCase):
    def test_one(self):
        tests: list = read_file("tests/ch01/test.json")
        for case in tests:
            message: str = case["message"]
            expected: str = case["expected"]
            words: list = message.strip().lower().split(" ")
            result: str = solve(words)
            self.assertEqual(result, expected)
