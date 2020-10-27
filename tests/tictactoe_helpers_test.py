import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

import tictactoe_helpers 


class GeneralTestCase(unittest.TestCase):
   def __init__(self, methodName, param1=None, param2=None):
       super(GeneralTestCase, self).__init__(methodName)
       self.param1 = param1
       self.param2 = param2

   def runInputPlayerLetterTest(self):
       result = tictactoe_helpers.inputPlayerLetter(self.param1)
       self.assertIn(result, [['X', 'O'],['O','X']])
       pass  # Test that depends on param 1 and 2.
   
   def runWhoGoesFirstTest(self):
       result = tictactoe_helpers.whoGoesFirst()
       #print("{}",result)
       self.assertIn(result, ('PlayerTurn','ComputerTurn'))
       pass  # Test that depends on param 1 and 2.

   def runPlayAgainTest(self):
       result = tictactoe_helpers.playAgain(self.param1)
       self.assertTrue(result)
       pass  # Test that depends on param 1 and 2.
 
   def runNegativePlayAgainTest(self):
       result = tictactoe_helpers.playAgain(self.param1)
       self.assertFalse(result)
       pass  # Test that depends on param 1 and 2.

def load_tests(loader, tests, pattern):
    test_cases = unittest.TestSuite()
    for p1, p2 in [('X', 'O'), ('O','X')]:
        test_cases.addTest(GeneralTestCase('runInputPlayerLetterTest', p1, p2))
    
    test_cases.addTest(GeneralTestCase('runWhoGoesFirstTest'))
    
    for p1 in ['Yes', 'Y']:
        test_cases.addTest(GeneralTestCase('runPlayAgainTest', p1))
    for p1 in ['P', '?','4','certainly']:
        test_cases.addTest(GeneralTestCase('runNegativePlayAgainTest', p1))
    return test_cases


if __name__ == '__main__':
   # Find all files matching pattern
   module_files = sorted(glob.glob(test_pattern))
   module_names = [os.path.splitext(os.path.basename(module_file))[0] for module_file in module_files]

   # Iterate over the found files
   print('Importing:')
   for module in module_names:
       print('    ', module)
       exec('import %s' % module)

   print('Done!')
   print()
   unittest.main(defaulTest=module_names)
