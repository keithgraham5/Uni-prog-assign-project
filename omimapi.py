

import requests
"""

/api/[handler]?[parameters]
/api/[handler]/[component]?[parameters]
/api/[handler]/[action]?[parameters]
The handler refers to the data object, such as an entry or a 
clinical synopsis.
The component is optional and refers to a specific data component 
within a data object for example references within an entry.
The action is optional and refers to an action to be performed
on a data object, such as a search for entries.

The OMIM API is located at https://api.omim.org/api
"""

#import modules
import requests
import json

#Create a function with an API request with one arguement
def make_request(mimNumber):
    query = "https://api.omim.org/api/clinicalSynopsis?mimNumber=%s&apiKey=0K24hSeBQfSAMi6cmcs-Rg&format=json" % mimNumber
    print(query)
    response = requests.get(query)
    return response
omim_response = make_request("100100")
omim_data = omim_response.json()

#converts our python object(clincal synopsis)into a formatted json string and prints
print(json.dumps(omim_data, sort_keys=True, indent=4, separators=(',', ': ')))



