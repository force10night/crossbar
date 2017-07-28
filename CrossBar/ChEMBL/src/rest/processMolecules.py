'''
Created on 20 Jul 2017

@author: anight
'''
#https://www.dataquest.io/blog/python-json-tutorial/
#https://www.ebi.ac.uk/chembl/api/data/molecule.json
import ijson
import pandas as pd

# molecules is a link list of json formatted data
def processMolecules(molecules):
    
    
    parsingColumns = [
        "date_of_stop", 
        "time_of_stop", 
        "agency"
    ]

    objects = ijson.items(molecules, 'molecule.columns.item')
    columns = list(objects)
    column_names = [col["fieldName"] for col in columns]
    
    parseData = []
    jObjects = ijson.items(molecules, 'molecule.item')
    for row in jObjects:
        processedRow = []
        for item in parsingColumns:
            processedRow.append(row[column_names.index(item)])
        parseData.append(processedRow)    
        
    print(molecules)
    df = pd.read_json(parseData,columns=parsingColumns)
    
    
# here need to go through the json and extract out what we need into a tsv file
