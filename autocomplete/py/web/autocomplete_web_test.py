#!/usr/bin/env python3

import unittest
from autocomplete_web import binary_search, read_lines


class TestAutoComplete(unittest.TestCase):

    def test_binary_search(self):
        lines = ["aaaaa", "bbbbbbb", "ccccccccc", "dddddddd", "eeeeeee", "fffffff", "ggggggg"]
        self.assertEqual(binary_search(lines, "aaaa", 0, len(lines) - 1), 0)
        self.assertEqual(binary_search(lines, "c", 0, len(lines) - 1), 2)
        self.assertEqual(binary_search(lines, "ggg", 0, len(lines) - 1), 6)

    def test_read_lines(self):
        lines = read_lines()
        self.assertGreater(len(lines), 100)
        
if __name__ == '__main__':
    unittest.main()
