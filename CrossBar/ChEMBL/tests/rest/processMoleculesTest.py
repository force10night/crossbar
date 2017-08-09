'''
Created on 31 Jul 2017

@author: anight
'''
import unittest
from rest import processMolecules as process



def testprocessMoleculesJson():
    jsonFile = '/Users/anight/crossbar/CrossBar/ChEMBL/resources/molecules.json'
    
    with open(jsonFile, 'r') as f:
        process.__process_Molecules__(f)
        return "good"
    

class processMoleculesTest(unittest.TestCase):


    def testName(self):
        self.assertTrue(testprocessMoleculesJson(), "good")
        print("test finished")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()