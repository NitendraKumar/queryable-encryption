# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:36:28 2023

@author: Nitendra.Kumar
"""

from pymongo import MongoClient
from your_credentials import get_credentials


import time
import pprint
from  data_creator import prepare10KRecords

def current_milli_time():
    return round(time.time() * 1000)


credentials = get_credentials()
connection_string = credentials["MONGODB_URI"]


regularClient = MongoClient(connection_string)

# data = prepare10KRecords()


# start = current_milli_time()
# for doc in  data:
#     regularClient.medicalRecords_un.patients_un.insert_one(doc)

# end = current_milli_time()
# print("regular insertion time for 10K records", (end-start))


start = current_milli_time()
result2 = regularClient.medicalRecords_un.patients_un.find_one({"ssn": 20})
end = current_milli_time()
print("regular time ssn : ", (end-start))
print("------------------")
pprint.pprint(result2)
