import unittest


def is_even(number):
    """ Returns True if **number** is even or False if it is odd. """
    return number % 2


class TestPossibilityOfLecture(unittest.TestCase):
    """
    The test is designed to determine the lecture will be canceled or not.
    """
    def setUp(self):
        self.T = int(input())
        self.N, self.K = list(map(int, input().split()))
        self.S = list(map(int, input().split()))
        print(self.T, self.N, self.K, self.S)
        
    def test_number_of_tests(self):
        self.assertTrue(self.T <= 5)
    '''
    def test_number_of_tests(self):
        self.assertIs(type(is_even(2)), bool)
        
    def test_no_arg(self):
        with self.assertRaises(TypeError):
            is_even()
    
    def test_is_even(self):
        #True if **number** is even
        self.assertTrue(is_even(2))
        
    def test_is_odd(self):
        # False if **number** is odd
        self.assertFalse(is_even(3))

    def test_float(self):
        # Parity is a property of an integer
        with self.assertRaises(TypeError):
            is_even(2.3)
    '''
            
if __name__ == '__main__':
    unittest.main()
