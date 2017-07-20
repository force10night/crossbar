'''
Created on 20 Jul 2017

@author: anight
'''


import json
import argparse
import requests
import time
from functools import wraps
#import resource
import logging


 
        
        
def chemblGetData(url):
        """ 
        Getting Chembl data
        Return JSON object.
        """
        data = requests.get(url)
        return data   
    
def getData2(url):
        headers = {'Content-Type':'application/json',}
        orderList = []
        response = requests.get(url).json()
        orderList.append(response)
        num_pages = response['last_page']
        while requests.get('hasMore') == True:
            print('new page\n')
            response = requests.get(url.format(response['nextPageUrl'])).json()
            orderList.append(response)
        return orderList



def chemblRestQueries():
        moleculeUrl = 'https://www.ebi.ac.uk/chembl/api/data/molecule?format=json' 
        # moleculesJson = self.getData2(moleculeUrl)
        moleculesJson = chemblGetData(moleculeUrl)
        print(json.dumps(moleculesJson, indent=4))
