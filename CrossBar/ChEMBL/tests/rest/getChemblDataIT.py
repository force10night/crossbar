'''
Created on 20 Jul 2017

@author: anight
'''
import unittest
import json
from rest import getChemblData as get



def testgetChemblData2Impl():
    moleculeUrl = 'https://www.ebi.ac.uk/chembl/api/data/molecule?format=json' 
    moleculesJson = get.chemblGetData(moleculeUrl)
    print(moleculesJson)
    data = json.loads(moleculesJson)

    
    return "good"

class getChemblDataIT(unittest.TestCase):


    def testgetChemblData2(self):
        self.assertTrue(testgetChemblData2Impl(), "good")
        print("test finished")
 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testgetChemblData2']
    unittest.main()