#import modules
import requests
import json
# Create function using keyword def, function name is make_request
#information passed to function as arguments seperated by comma.
def make_request(base_url="https://rest.variantvalidator.org/VariantValidator/variantvalidator",
                 variant="NM_000088.3:c.589G>T",
                 genome_build="GRCh37",
                 select_transcripts="all"):

#query is a variable to which the paramaters in brackets are passed the
    query = "%s/%s/%s/%s" % (base_url, genome_build, variant, select_transcripts)
    # Tell the User the full URL of their call to the rest API
    print("Querying VariantValidator API with URL: " + query)
    # Make the request and pass to a response object that the function returns
    response = requests.get(query)
    return response
# Use the function in example, where the key-worded variables are pre-populated
vv_response = make_request()
data = vv_response.json()
#rint(json.dumps(data,indent=4, separators=(' ', '=')))

