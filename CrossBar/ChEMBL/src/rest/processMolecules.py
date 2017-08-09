'''
Created on 20 Jul 2017

@author: anight
'''
#https://www.dataquest.io/blog/python-json-tutorial/
#https://www.ebi.ac.uk/chembl/api/data/molecule.json
import ijson
import pandas as pd


#class processMoleculest():
#    def __init__(self):
       

# molecules is a link list of json formatted data
def __process_Molecules__(molecules):


    __molecule_Columns__ = [
        "max_phase", 
        "usan_stem",
        "parenteral", 
        "withdrawn_flag", 
        "dosed_ingredient", 
        "molecule_type", 
        "withdrawn_reason", 
        "biotherapeutic", 
        "chebi_par_id", 
        "withdrawn_country", 
        "first_approval", 
        "atc_classifications", 
        "prodrug", 
        "molecule_structures",
        "chirality", 
        "usan_substem", 
        "pref_name", 
        "polymer_flag", 
        "molecule_chembl_id", 
        "therapeutic_flag", 
        "molecule_properties",
        "structure_type", 
        "helm_notation", 
        "usan_stem_definition", 
        "natural_product", 
        "black_box_warning", 
        "availability_type", 
        "inorganic_flag", 
        "molecule_synonyms", 
        "withdrawn_year", 
        "molecule_hierarchy", 
        "indication_class", 
        "usan_year", 
        "first_in_class", 
        "topical", 
        "oral"
    ]

    
    __mol_Props__ = [
        "mw_freebase",
        "rtb",
        "acd_logd",
        "full_molformula",
        "hbd_lipinski",
        "num_lipinski_ro5_violations",
        "alogp",
        "acd_most_apka",
        "acd_logp",
        "heavy_atoms",
        "aromatic_rings",
        "hba_lipinski",
        "num_ro5_violations",
        "psa",
        "mw_monoisotopic",
        "acd_most_bpka",
        "ro3_pass",
        "num_alerts",
        "hbd",
        "hba",
        "molecular_species",
        "full_mwt",
        "qed_weighted"
        ]
    
    
    __parsed_Mol_Columns__ = [
       "max_phase",
       "withdrawn_flag", 
       "dosed_ingredient", 
       "molecule_type", 
       "biotherapeutic", 
       "chebi_par_id", 
       "prodrug",
       "chirality", 
       "usan_substem", 
       "pref_name", 
       "molecule_chembl_id", 
       "therapeutic_flag",
       "structure_type", 
       "natural_product", 
       "black_box_warning", 
       "inorganic_flag", 
       "molecule_synonyms",
       "standard_inchi_key",
       "canonical_smiles",
       "standard_inchi",
       "molecule_chembl_id",
       "parent_chembl_id",
       "mw_freebase",
       "rtb",
       "acd_logd",
       "full_molformula",
       "hbd_lipinski",
       "num_lipinski_ro5_violations",
       "alogp",
       "heavy_atoms",
       "aromatic_rings",
       "hba_lipinski",
       "num_ro5_violations",
       "mw_monoisotopic",
       "ro3_pass",
       "num_alerts",
       "hbd",
       "hba",
       "molecular_species",
       "full_mwt"
        ]
    
# Arrays defining which data fields to extract 
#objects = ijson.items(molecules, 'molecule.columns.item')


    __parsing_Columns__ = [
       "max_phase",
       "withdrawn_flag", 
       "dosed_ingredient", 
       "molecule_type", 
       "biotherapeutic", 
       "chebi_par_id", 
       "prodrug",
       "chirality", 
       "usan_substem", 
       "pref_name", 
       "molecule_chembl_id", 
       "therapeutic_flag",
       "structure_type", 
       "natural_product", 
       "black_box_warning", 
       "inorganic_flag", 
       "molecule_synonyms"
       ]
    
    __mol_Structs__ = [
       "standard_inchi_key",
       "canonical_smiles",
       "standard_inchi"
       ]
    
    __mol_Hier_ = [
       "molecule_chembl_id",
       "parent_chembl_id"
       ]
    
    __parse_Props__ = [    
       "mw_freebase",
       "rtb",
       "acd_logd",
       "full_molformula",
       "hbd_lipinski",
       "num_lipinski_ro5_violations",
       "alogp",
       "heavy_atoms",
       "aromatic_rings",
       "hba_lipinski",
       "num_ro5_violations",
       "mw_monoisotopic",
       "ro3_pass",
       "num_alerts",
       "hbd",
       "hba",
       "molecular_species",
       "full_mwt"
       ]
    parseData = []
    
    jObjects = ijson.items(molecules,'item')
   
    for row in jObjects:
        processedRow = []
    #   print(row)
        for f in __parsing_Columns__:
        #   print(row[f])
            processedRow.append(row[f])
        for ele in __mol_Structs__:
        #    print(row["molecule_structures"][ele])
            processedRow.append(row["molecule_structures"][ele])
        for ele in __mol_Hier_:
        #    print(row["molecule_hierarchy"][ele])
            processedRow.append(row["molecule_hierarchy"][ele])
        for ele in __parse_Props__:
        #   print(row["molecule_properties"][ele])
            processedRow.append(row["molecule_properties"][ele])
        # print(processedRow)     
        parseData.append(processedRow)               
        
    return pd.DataFrame(parseData, columns=__parsed_Mol_Columns__)
    
    # print(df)
    # df = pd.read_json(parseData,columns=parsingColumns)


    # here need to go through the json and extract out what we need into a tsv file
