import unittest
import imsys , imsys2
class TestIMSystem(unittest.TestCase):

    #tests to see if a connection is established
    #def test_connectMySQL(self):
    #    self.assertRaises(Exception, imsys.connectMySQL, True)
    
    #tests for an established connection with mySQL server
    def test_connectMySQL2(self):
        result = imsys.connectMySQL(True)
        self.assertEqual(result, True)

    def test_menuExit(self):
        resultexitTrue = imsys2.exitToMenu(0)
        resultexitFalse = imsys2.exitToMenu(1)
        self.assertEqual(resultexitTrue, True)
        self.assertEqual(resultexitFalse, False)
if __name__ == '__main__':
    unittest.main()
