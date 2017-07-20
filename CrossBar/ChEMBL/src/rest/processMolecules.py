'''
Created on 20 Jul 2017

@author: anight
'''

import json

def processMolecules(molecules):
    print(json.dumps(molecules, indent=4))
# here need to go through the json and extract out what we need into a tsv file
    data = json.loads(molecules, object_hook=JSONObject)