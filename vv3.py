# import modules
import requests
import json

import json
"""
This is the web path (URL) for the VariantValidator API 
The VariantValidator API is located at https://rest.variantvalidator.org
The VariantValidator endpoints are located under the /VariantValidator/ name space
The variantvalidator endpoint is found at /VariantValidator/variantvalidator/
"""
#Create a function with an  API request to variant validator using 3 arguments.
def make_request(base_url="https://rest.variantvalidator.org/VariantValidator/variantvalidator",
                 variant="NM_000088.3:c.589G>T",
                 genome_build="GRCh37",
                 select_transcripts="all"):
    """
    :param base_url: Defined above
    :param variant: A variant description (https://variantvalidator.org/service/validate/ for accepted formats)
    :param genome_build: Cpecify a genome build (GRCh37 or GRCh38)
    :param select_transcripts: This allows us to specify a specific transcript for a genomic variant if we wish
    :return: JSON of the variantvalidator output
    """
    # https://rest.variantvalidator.org/VariantValidator/variantvalidator/GRCh37/NM_000088.3%3Ac.589G%3ET/all?content-type=application%2Fjson
    # Create call using string formatting
    query = "%s/%s/%s/%s" % (base_url, genome_build, variant, select_transcripts)
    # Tell the User the full URL of their call to the rest API
    #print("Querying VariantValidator API with URL: " + query)
    # Sending a .get request to a specific url save the saves and returns the response variable response
    response = requests.get(query)
    return response

# Use the function in example, where the key-worded variables are pre-populated
vv_response = make_request()
data = vv_response.json()


#converts our python object into a formatted json string and prints
print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
#interating through json string item to find key
for key, val in data.items():
    try:
        if "gene_symbol" in val.keys():
            print(val['gene_symbol'])
    except AttributeError:
        continue