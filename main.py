import pandas as pd
import numpy as np
import requests
import json

# api key from dictionaryapi.com
api_key = "a2071270-0839-467f-9bc9-963ca972f853"

def punbot (word1, word2):
    payload = {
        "key":api_key
    }

    url1="https://www.dictionaryapi.com/api/v3/references/thesaurus/json/"+word1
    url2="https://www.dictionaryapi.com/api/v3/references/thesaurus/json/"+word2

    request1 = requests.request("GET",url1,params=payload)
    syns1 = request1.json()[0]['meta']['syns']
    print(syns1)
    
    request2 = requests.request("GET",url2,params=payload)
    syns2 = request2.json()[0]['meta']['syns']
    print(syns2)
    
    if len(syns1[0])>len(syns2[0]):
        main = syns2
        second = syns1
    else:
        main = syns1
        second = syns2

    for x in main[0]:
        for i in second[0]:
            print(x+" "+i)




punbot("dog","walker")
