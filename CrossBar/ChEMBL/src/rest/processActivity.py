'''
Created on 20 Jul 2017

@author: anight
'''
#https://www.ebi.ac.uk/chembl/api/data/activity.json
import ijson
import pandas as pd


#class processMoleculest():
#    def __init__(self):
       

# molecules is a link list of json formatted data
def __process_Activities__(activities):


  


    __activity_Columns__ = [
        "document_journal", 
        "bao_endpoint", 
        "potential_duplicate", 
        "uo_units", 
        "canonical_smiles", 
        "assay_type", 
        "src_id", 
        "ligand_efficiency", 
        "standard_flag", 
        "molecule_chembl_id", 
        "target_organism", 
        "assay_description", 
        "record_id", 
        "document_chembl_id", 
        "bao_format", 
        "standard_units", 
        "activity_id", 
        "standard_type", 
        "target_chembl_id", 
        "data_validity_comment", 
        "standard_relation", 
        "document_year", 
        "target_pref_name", 
        "assay_chembl_id", 
        "published_value", 
        "published_relation", 
        "standard_value", 
        "qudt_units", 
        "published_units", 
        "pchembl_value", 
        "published_type", 
        "activity_comment"
         ]
        
        
        
        

    
    
    
    __parsing_Act_Columns__ = [
        "bao_endpoint", 
        "potential_duplicate", 
        "uo_units", 
        "assay_type", 
        "ligand_efficiency", 
        "standard_flag", 
        "molecule_chembl_id", 
        "target_organism", 
        "record_id", 
        "document_chembl_id", 
        "bao_format", 
        "standard_units", 
        "activity_id", 
        "standard_type", 
        "target_chembl_id", 
        "data_validity_comment", 
        "standard_relation", 
        "assay_chembl_id", 
        "published_value", 
        "published_relation", 
        "standard_value", 
        "published_units", 
        "pchembl_value" 
        ]
    
# Arrays defining which data fields to extract 
#objects = ijson.items(molecules, 'molecule.columns.item')

   
    parseData = []
    
    jObjects = ijson.items(activities,'item')
      
    for row in jObjects:
        processedRow = []
    #   print(row)
        for f in __parsing_Act_Columns__:
        #   print(row[f])
            processedRow.append(row[f])
        # print(processedRow)     
        parseData.append(processedRow)               
        
    return pd.DataFrame(parseData, columns=__parsing_Act_Columns__)
    
    # print(df)
