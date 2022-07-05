#!/usr/bin/python3

import unittest

from se_solver import get_input_data, se_solve

class TestSeSolver(unittest.TestCase):
    """Calc tests"""    
    def test_get_input_data(self):
    
        self.assertEqual(get_input_data(['hghg', '1', '2', '3', '4']), [[1, 2, 3], [4]], "Should be [[1, 2, 3], [4]]")
    
    
    def test_get_input_data_empty(self):
        self.assertEqual(get_input_data(['hghg']), [], "Should be []")



if __name__ == '__main__':
    unittest.main()



# from se_solver import get_input_data

# if get_input_data(['hghg', '1', '2', '3', '4']) != [[1, 2, 3], [4]]:
#     raise Exception('Функция работает неверно!')
