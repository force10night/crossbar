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
from pyasn1.compat.octets import null


 
        
        
def chemblGetData(url):
        """ 
        Getting Chembl data
        Return JSON object.
        """
        data = requests.get(url)
        return data   
    
def getData2(baseUrl, service):
        urlFormat = "format=json"
        startCount = 0
        resultsCount = startCount
        maxResultsPerPage = 20
        startAt = "startAt=" + str(startCount)
        resultsPerPage = "maxResults=" + str(maxResultsPerPage)
        orderedList = list()
        
        fullUrl = baseUrl + "/" + service + "?" + startAt + "&" + resultsPerPage + "&" + urlFormat
        
        while True:
            response = requests.get(fullUrl)
            #print(response.text)
            jsonResponse = json.loads(response.text)
            orderedList.append(jsonResponse["molecules"])
            page_info = jsonResponse["page_meta"]
            # print(page_info["next"])
            if page_info["next"] is None or (resultsCount >= page_info["total_count"]):
                break
            
            resultsCount += maxResultsPerPage
            fullUrl = baseUrl + page_info["next"] 
          
        print("total results count = " + str(resultsCount))     
        return orderedList



def chemblRestQueries():
        moleculeUrl = 'https://www.ebi.ac.uk/chembl/api/data/molecule?format=json' 
        # moleculesJson = self.getData2(moleculeUrl)
        moleculesJson = chemblGetData(moleculeUrl)
        print(json.dumps(moleculesJson, indent=4))
