'''
Created on 31 Jul 2017

@author: anight
'''
import unittest
from rest import processAssay as process



def testprocessAssaysJson():
    jsonFile = '/Users/anight/crossbar/CrossBar/ChEMBL/resources/assays.json'
    
    with open(jsonFile, 'r') as f:
        process.__process_Assays__(f)
        return "good"
    

class processAssaysTest(unittest.TestCase):


    def testName(self):
        self.assertTrue(testprocessAssaysJson(), "good")
        print("test finished")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()