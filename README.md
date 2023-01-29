# queryable-encryption
MongoDB- Queryable Encryption
* This repository has been forked from original mongodb enrypted encryption tutorialhttps://github.com/mongodb-university/docs-in-use-encryption-examples.git
* Runnable on window machine with client side field level encryption using mongocryptd native librar.

## Setup instructions
Step 1- 
* Install python requirements
* Install mongodb
* Install mongosh
Step 2-
* Start mongo server- run cmd > mongosh 
* Prepare master-key file-  run cmd > openssl rand 96 > master-key.txt
* Find location of mongocryptd lib in your installation directory
** example : C:/Program Files/MongoDB/Server/6.0/bin/mongocryptd.exe
* Configure MONGO url and mongod lib in your_credentials.py
Step 3-
* Prepare encryption key by running python file "make_data_key.py file"
* copy the data encryption key from console
* set dek_id parameter in "insert_encrypted_document.py" file.
* run "insert_encrypted_document.py" to insert and query the documents.
Step 4-
* Verify your data from mongosh console
* To show all available database in monog run > show dbs
* To select specific db > use [db_name from above list]
* To show all the available collection in selected db > db.getCollectionNames()
* To run query on specific collection > db.[collection name].fineOne() for one document

