#!/usr/bin/python3

import unittest

from se_solver import get_input_data, se_solve, make_se_text
from se_solver import RC_NO_ROOTS, RC_NOT_A_SE, RC_ONE_ROOT, RC_TWO_ROOTS


class TestSeSolver(unittest.TestCase):
    """
    Tests for se_solver.py script
    """

    def test_get_input_data(self):
        """
        Make sure arguments from command line are converted into the list of triads correctly
        """
        self.assertEqual(get_input_data(['script name', '1', '2', '3', '4']), [[1, 2, 3], [4, 0, 0]], "Should be [[1, 2, 3], [4, 0, 0]]")
        self.assertEqual(get_input_data(['script name', '1', '2', '3', '4', '5']), [[1, 2, 3], [4, 5, 0]], "Should be [[1, 2, 3], [4, 5, 0]]")
    
    
    def test_get_input_data_empty(self):
        """
        No arguments should lead to empty list of triads
        """
        self.assertEqual(get_input_data(['script name']), [], "Should be []")

    def test_not_a_se(self):
        """
        If the first of the three is zero then result should be RC_NOT_A_SE
        """
        self.assertEqual(se_solve(1, 4, 5)[0], RC_NOT_A_SE, "Should be -1")

    def test_no_roots(self):
        """
        Check that we correctly solved the equation with no roots
        """
        self.assertEqual(se_solve(10, -1, 2)[0], RC_NO_ROOTS, "Should be 0")

    def test_one_root(self):
        """
        Check that we correctly solved the equation with one root
        """
        self.assertEqual(se_solve(-4, 12, -9)[0], RC_ONE_ROOT, "Should be 1")

    def test_two_roots(self):
        """
        Check that we correctly solved the equation with two roots
        """
        self.assertEqual(se_solve(2, 5, -2)[0], RC_TWO_ROOTS, "Should be 2")

    def test_make_se_text(self):
        """
        check if we can costruct the equation text correctly using different variants of arguments
        """
        self.assertEqual(make_se_text(-1, 5, -2), "x^2 + 5x - 2 = 0", "Should be 'x^2 + 5x - 2 = 0'")
        self.assertEqual(make_se_text(1, 5, -2), "x^2 + 5x - 2 = 0", "Should be 'x^2 + 5x - 2 = 0'")
        self.assertEqual(make_se_text(1, 0, -2), "x^2 - 2 = 0", "Should be 'x^2 - 2 = 0'")
        self.assertEqual(make_se_text(1, 5, 0), "x^2 + 5x = 0", "Should be 'x^2 + 5x = 0'")
        self.assertEqual(make_se_text(4, -5, 6), "4x^2 - 5x + 6 = 0", "Should be '4x^2 - 5x + 6 = 0'")
        self.assertEqual(make_se_text(4, 5, -6), "4x^2 + 5x - 6 = 0", "Should be '4x^2 + 5x - 6 = 0'")

if __name__ == '__main__':
    unittest.main()

