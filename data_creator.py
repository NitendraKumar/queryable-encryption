# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:12:39 2023

@author: Nitendra.Kumar
"""
import random

name_list = ["James	4663035", "Mary	3124584", "Robert	4407377", "Patricia	1555054", "John	4403862", "Jennifer	1469031", "Michael 4340931", "Linda	1448283", "David	3564313", "Elizabeth	1411916", "William	3524670", "Barbara	1391959", "Richard	2439835", "Susan	1103018", "Joseph	2317860", "Jessica	1047000", "Thomas	2143281", "Sarah	989810", "Charles	2060835", "Karen	986072", "Christopher	2044437", "Lisa	965015", "Daniel	1900488", "Nancy	963833", "Matthew	1614109", "Betty	906997", "Anthony	1407623", "Margaret	892334", "Mark	1348322", "Sandra	873655", "Donald	1323467", "Ashley	851020", "Steven	1283686", "Kimberly	841144", "Paul	1263912", "Emily	835442", "Andrew	1255723", "Donna	821223", "Joshua	1226213", "Michelle	813153", "Kenneth	1212646", "Carol	804807", "Kevin	1176784", "Amanda	773501", "Brian	1169267", "Dorothy	772958", "George	1110560", "Melissa	754784", "Timothy	1072620", "Deborah	740223", "Ronald	1072270", "Stephanie	738905", "Edward	1060576", "Rebecca	729447", "Jason	1041127", "Sharon	720831", "Jeffrey	976651", "Laura	714847", "Ryan	947756", "Cynthia	705778", "Jacob	941181", "Kathleen	683064", "Gary	900277", "Amy	682347", "Nicholas	896856", "Angela	659597", "Eric	880874", "Shirley	657764", "Jonathan	853162", "Anna	607022", "Stephen	838395", "Brenda	606299", "Larry	802063", "Pamela	592699", "Justin	781577", "Emma	591173", "Scott	770208", "Nicole	590414", "Brandon	763634", "Helen	584461", "Benjamin	749881", "Samantha	581626", "Samuel	717912", "Katherine	568258", "Gregory	707931", "Christine	558861", "Alexander	683727", "Debra	548281", "Frank	675530", "Rachel	545873", "Patrick	665520", "Carolyn	539223", "Raymond	657165", "Janet	537105", "Jack	635483", "Catherine	534876", "Dennis	610810", "Maria	529993",
             "Jerry	601368", "Heather	524171", "Tyler	594971", "Diane	515112", "Aaron	588205", "Ruth	514443", "Jose	565276", "Julie	506856", "Adam	557653", "Olivia	498779", "Nathan	554162", "Joyce	497784", "Henry	552869", "Virginia	496631", "Douglas	546783", "Victoria	489302", "Zachary	543288", "Kelly	471945", "Peter	537153", "Lauren	471879", "Kyle	482101", "Christina	471224", "Ethan	453826", "Joan	465670", "Walter	452806", "Evelyn	457188", "Noah	445870", "Judith	449739", "Jeremy	440663", "Megan	438147", "Christian	434517", "Andrea	437735", "Keith	430900", "Cheryl	436888", "Roger	427016", "Hannah	435256", "Terry	422105", "Jacqueline	420410", "Gerald	421918", "Martha	417402", "Harold	421631", "Gloria	406375", "Sean	420553", "Teresa	403870", "Austin	418592", "Ann	402317", "Carl	418263", "Sara	400065", "Arthur	399784", "Madison	399308", "Lawrence	396484", "Frances	399109", "Dylan	390694", "Kathryn	398924", "Jesse	387393", "Janice	398820", "Jordan	386325", "Jean	390826", "Bryan	383979", "Abigail	388793", "Billy	376747", "Alice	387931", "Joe	376613	", "Julia	378548", "Bruce	375068	", "Judy	377609", "Gabriel	366152	", "Sophia	376519", "Logan	359286	", "Grace	376006", "Albert	358151	", "Denise	371271", "Willie	354624	", "Amber	371156", "Alan	351694	", "Doris	370008", "Juan	349098	", "Marilyn	369504", "Wayne	335173	", "Danielle	369198", "Elijah	329248	", "Beverly	368510", "Randy	328337	", "Isabella	365383", "Roy	326203	", "Theresa	364816", "Vincent	323623	", "Diana	360717", "Ralph	321289	", "Natalie	359738", "Eugene	316285	", "Brittany	359143", "Russell	315198	", "Charlotte	357576", "Bobby	313130	", "Marie	349383", "Mason 312464	", "Kayla	341740", "Philip	311366	", "Alexis	341562", "Louis	308706	", "Lori	337993"]
blood_types = ["A", "B", "AB+","A-", "B+", "O+", "O-"]
providers = ["prover_A", "provide_B","provider_C", "provider_D"]

def prepare10KRecords():
    data = []
    
    for i in range(1, 100000):
        insurance = {"policyNumber": i, "provider": providers[random.randint(0,3)]}
        medical_record = [{"weight": 180, "bloodPressure": "120/80"}]
        doc = {
             "name": name_list[random.randint(0, 99)],
             "ssn": i,
             "bloodType": blood_types[random.randint(0,6)],
             "medicalRecords": medical_record, 
             "insurance": insurance,
             "key-id": "demo-data-key",
         }
        data.append(doc)
    return data