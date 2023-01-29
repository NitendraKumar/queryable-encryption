from pymongo import MongoClient
from pymongo.encryption_options import AutoEncryptionOpts
from pymongo.encryption import ClientEncryption
import base64
import os
from bson.codec_options import CodecOptions
from bson.binary import STANDARD, UUID, UUID_SUBTYPE, Binary
import pprint
from your_credentials import get_credentials
from data_creator import prepare10KRecords

import time

def current_milli_time():
    return round(time.time() * 1000)


credentials = get_credentials()

# start-key-vault
key_vault_namespace = "encryption.__keyVault"
# end-key-vault

connection_string = credentials["MONGODB_URI"]

# start-kmsproviders
path = "./master-key.txt"
with open(path, "rb") as f:
    local_master_key = f.read()
kms_providers = {
    "local": {
        "key": local_master_key  # local_master_key variable from the previous step
    },
}
# end-kmsproviders

# start-schema
# Make All fields random to use json pointer to reference key-id
dek_id = b"legt+l9bSJOWPP4kvaZCMw=="
json_schema = {
    "bsonType": "object",
    "encryptMetadata": {"keyId": [Binary(base64.b64decode(dek_id), UUID_SUBTYPE)]},
    "properties": {
        "insurance": {
            "bsonType": "object",
            "properties": {
                "policyNumber": {
                    "encrypt": {
                        "bsonType": "int",
                        "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
                    }
                }
            },
        },
        "medicalRecords": {
            "encrypt": {
                "bsonType": "array",
                "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
            }
        },
        "bloodType": {
            "encrypt": {
                "bsonType": "string",
                "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
            }
        },
        "ssn": {
            "encrypt": {
                "bsonType": "int",
                "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
            }
        },
    },
}
patient_schema = {"medicalRecords.patients": json_schema}
# end-schema


# start-extra-options
extra_options = {"mongocryptd_spawn_path": credentials["MONGOCRYPTD_PATH"]}
# end-extra-options

# start-client
fle_opts = AutoEncryptionOpts(
    kms_providers, key_vault_namespace, schema_map=patient_schema, **extra_options
)
secureClient = MongoClient(connection_string, auto_encryption_opts=fle_opts)
# end-client

# start-insert
# def insert_patient(collection, doc):
#     collection.insert_one(doc)

# data = prepare10KRecords()
# start = current_milli_time()
# for doc in data:
#     insert_patient(secureClient.medicalRecords.patients,doc)

# end = current_milli_time()
# print("Encrypted insertion time for 10K records : ", (end-start))

    
    
    
    
# # end-insert
# regularClient = MongoClient(connection_string)
# # start-find
# print("Finding a document with regular (non-encrypted) client.")
# start = current_milli_time()
# result = regularClient.medicalRecords.patients.find_one({"name": "Jon Doe"})
# end = current_milli_time()
# print("Regular find : ", (end-start))
# # pprint.pprint(result)

print("Finding a document with encrypted client, searching on an encrypted field")
start = current_milli_time()
result2 = secureClient.medicalRecords.patients.find_one({"ssn": 9997})
# result2 = regularClient.medicalRecords.patients.find_one({"ssn": 241014209})
end = current_milli_time()
print("Encrypted find : ", (end-start))
pprint.pprint(result2)


