Using a API request to GET gene_ids and omim_id from varaiant validator @ variantvalidator.org. Obtained omim_id from varaintvalidator is used a part of a GET API request to the Online Mendelian Inheritance in Man at OMIM.org to obtain a Clinical synopsis/ genotype-phenotype correlation. The gene_ids from varaint validator and the Clinical Synopsis from Mendelian Inheritance in Man is cross referenced against the list of gene panels obtained using an API to GET requesst from the Genoimcs england panel app @ https://panelapp.genomicsengland.co.uk/


File 
vv3.py  omimapi.py  gepanelapi.py


vv.3.py 
Inputs: Enter the your variant of interest into make_request function along with the genome build and transcript selection.  
Outputs: gene_id, (completed) passed to gepanelapi.py
Output: omim_id (not completed) passed to omimapi.py (not completed)
Exception handling loop - loop through the json is slower but if the formation of the json changes in the future the code will be able to handle it. Directly access the the value with dic key is much faster, but if the json format changes in the future the code will fail.

omimapi.py
input: Omim_id
output: clinical synopsis 

gepanal.py
input:gene_id (not complete)
output: list of gene panels (not complete)