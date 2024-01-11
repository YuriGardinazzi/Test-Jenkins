#!/bin/python3 

import sys
import pandas as pd
import numpy as np
import elabapi_python
import os
#import requests
###### CONFIG ######
API_KEY='1-f07d156b705ff46e9f45517c891888176ed2710de06a0de8bc9c4894bec95c539350bb2a62c0bace02ac1' 
API_HOST_URL = 'https://localhost:3148/api/v2'
###### END CONFIG ######


def try_api():
    '''
    Try the autogenerated library of elabftw for python.
    Code taken from the example on elabftw github 
    https://github.com/elabftw/elabapi-python/blob/master/examples/03.py#L11
    '''
    # Configure the api client
    configuration = elabapi_python.Configuration()
    configuration.api_key['api_key'] = API_KEY
    configuration.api_key_prefix['api_key'] = 'Authorization'
    configuration.host = API_HOST_URL
    configuration.debug = False
    configuration.verify_ssl = False

    # create an instance of the API class
    api_client = elabapi_python.ApiClient(configuration)
    # fix issue with Authorization header not being properly set by the generated lib
    api_client.set_default_header(header_name='Authorization', header_value=API_KEY)

    experimentsApi = elabapi_python.ExperimentsApi(api_client)
    uploadsApi = elabapi_python.UploadsApi(api_client)
    for i in range(len(experimentsApi.read_experiments())):
        print("ID: ",experimentsApi.read_experiments()[i].id)
    
    experimentId = experimentsApi.read_experiments()[i].id
    if experimentsApi.read_experiments()[i].category == "2":
        experimentsApi.patch_experiment(id=experimentId, body={'category':'3'})
    else:
        experimentsApi.patch_experiment(id=experimentId, body={'category':'2'})
     

    #print(thread)
    
if __name__ == "__main__":
    print("******START TESTING API******")
    try_api()
    print("******END TESTING API******")
