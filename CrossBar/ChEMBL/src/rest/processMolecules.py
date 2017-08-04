'''
Created on 20 Jul 2017

@author: anight
'''
#https://www.dataquest.io/blog/python-json-tutorial/
#https://www.ebi.ac.uk/chembl/api/data/molecule.json
import ijson
import pandas as pd


class processMolecules(object):
    def __init__(self):
        return self

    # molecules is a link list of json formatted data
    def __process_Molecules__(self,molecules):
    
    
        __molecule_Columns__ = [
           "atc_classifications",
           "availability_type",
           "biotherapeutic",
           "black_box_warning",
           "chebi_par_id",
           "chirality",
           "dosed_ingredient",
           "first_approval",
           "first_in_class",
           "helm_notation",
           "indication_class",
           "inorganic_flag",
           "max_phase",
           "molecule_chembl_id",
           "molecule_hierarchy.molecule_chembl_id",
           "molecule_hierarchy.parent_chembl_id",
           "molecule_properties.acd_logd",
           "molecule_properties.acd_logp",
           "molecule_properties.acd_most_apka",
           "molecule_properties.acd_most_bpka",
           "molecule_properties.alogp",
           "molecule_properties.aromatic_rings",
           "molecule_properties.full_molformula",
           "molecule_properties.full_mwt",
           "molecule_properties.hba",
           "molecule_properties.hba_lipinski",
           "molecule_properties.hbd",
           "molecule_properties.hbd_lipinski",
           "molecule_properties.heavy_atoms",
           "molecule_properties.molecular_species",
           "molecule_properties.mw_freebase",
           "molecule_properties.mw_monoisotopic",
           "molecule_properties.num_alerts",
           "molecule_properties.num_lipinski_ro5_violations",
           "molecule_properties.num_ro5_violations",
           "molecule_properties.psa",
           "molecule_properties.qed_weighted",
           "molecule_properties.ro3_pass",
           "molecule_properties.rtb",
           "molecule_structures.canonical_smiles",
           "molecule_structures.standard_inchi",
           "molecule_structures.standard_inchi_key",
           "molecule_synonyms.molecule_type",
           "molecule_synonyms.natural_product",
           "molecule_synonyms.oral",
           "molecule_synonyms.parenteral",
           "molecule_synonyms.polymer_flag",
           "molecule_synonyms.pref_name",
           "molecule_synonyms.prodrug",
           "molecule_synonyms.structure_type",
           "molecule_synonyms.therapeutic_flag",
           "molecule_synonyms.topical",
           "molecule_synonyms.usan_stem",
           "molecule_synonyms.usan_stem_definition",
           "molecule_synonyms.usan_substem",
           "molecule_synonyms.usan_year",
           "molecule_synonyms.withdrawn_country",
           "molecule_synonyms.withdrawn_flag",
           "molecule_synonyms.withdrawn_reason",
           "molecule_synonyms.withdrawn_year"
        ]

    #objects = ijson.items(molecules, 'molecule.columns.item')
    # columns = list(objects)
    # column_names = [col["fieldName"] for col in columns]
    
        __parsing_Columns__ = [
           "chebi_par_id",
           "chirality",
           "max_phase",
           "molecule_hierarchy.molecule_chembl_id",
           "molecule_hierarchy.parent_chembl_id",
           "molecule_properties.alogp",
           "molecule_properties.aromatic_rings",
           "molecule_properties.full_molformula",
           "molecule_properties.full_mwt",
           "molecule_properties.molecular_species",
           "molecule_structures.canonical_smiles",
           "molecule_structures.standard_inchi",
           "molecule_structures.standard_inchi_key",
           "molecule_synonyms.molecule_type",
           "molecule_synonyms.natural_product",
           "molecule_synonyms.pref_name",
           "molecule_synonyms.prodrug",
           "molecule_synonyms.structure_type",
           "molecule_properties.hba",
           "molecule_properties.hba_lipinski",
           "molecule_properties.hbd",
           "molecule_properties.hbd_lipinski",
        ]
        parseData = []
        jObjects = ijson.items(molecules, 'molecule.item')
        for row in jObjects:
            processedRow = []
            for item in __parsing_Columns__:
                processedRow.append(row[ __molecule_Columns__.index(item)])
            parseData.append(processedRow)  
        
            df = pd.DataFrame(parseData, columns=__parsing_Columns__)      
        
        print(df)
    # df = pd.read_json(parseData,columns=parsingColumns)
    
    
# here need to go through the json and extract out what we need into a tsv file
