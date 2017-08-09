'''
Created on 31 Jul 2017

@author: anight
'''
import unittest
from rest import processActivity as process



def testprocessActivitiesJson():
    jsonFile = '/Users/anight/crossbar/CrossBar/ChEMBL/resources/activity.json'
    
    with open(jsonFile, 'r') as f:
        process.__process_Activities__(f)
        return "good"
    

class processActivitiesTest(unittest.TestCase):


    def testName(self):
        self.assertTrue(testprocessActivitiesJson(), "good")
        print("test finished")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()