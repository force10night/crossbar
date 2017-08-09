'''
Created on 20 Jul 2017

@author: anight
'''
#https://www.ebi.ac.uk/chembl/api/data/assay.json
import ijson
import pandas as pd


#class processMoleculest():
#    def __init__(self):
       

# molecules is a link list of json formatted data
def __process_Assays__(assays):


  


    __assay_Columns__ = [
        "assay_category",
        "assay_cell_type",
        "assay_chembl_id",
        "assay_organism",
        "assay_strain",
        "assay_subcellular_fraction",
        "assay_tax_id",
        "assay_test_type",
        "assay_tissue",
        "assay_type",
        "assay_type_description",
        "bao_format",
        "cell_chembl_id",
        "confidence_description",
        "confidence_score",
        "description",
        "document_chembl_id",
        "relationship_description",
        "relationship_type",
        "src_assay_id",
        "src_id",
        "target_chembl_id",
        "tissue_chembl_id"
        ]
        
        
        
        

    
    
    
    __parsing_Ass_Columns__ = [
        "assay_category",
        "assay_cell_type",
        "assay_chembl_id",
        "assay_tax_id",
        "assay_test_type",
        "assay_tissue",
        "assay_type",
        "bao_format",
        "confidence_score",
        "document_chembl_id",
        "relationship_type",
        "src_assay_id",
        "target_chembl_id",
        "tissue_chembl_id"
        ]
    
# Arrays defining which data fields to extract 
#objects = ijson.items(molecules, 'molecule.columns.item')

   
    parseData = []
    
    jObjects = ijson.items(assays,'item')
      
    for row in jObjects:
        processedRow = []
    #   print(row)
        for f in __parsing_Ass_Columns__:
        #   print(row[f])
            processedRow.append(row[f])
        # print(processedRow)     
        parseData.append(processedRow)               
        
    return pd.DataFrame(parseData, columns=__parsing_Ass_Columns__)
    
    # print(df)
