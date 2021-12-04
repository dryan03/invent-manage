# this is my unit test file 

import unittest
import getSumFile

class TestGetSum(unittest.TestCase):
    def test_sum(self):
        result = getSumFile.getSum(5, 5)
        self.assertEqual(result, 20)
    

if __name__ == '__main__':
    unittest.main()
        
