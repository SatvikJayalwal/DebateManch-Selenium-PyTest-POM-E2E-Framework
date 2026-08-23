import os 
import json

def load_contact_us_data():
    file_path = os.path.join(os.getcwd(),"test_data_files","contact_us_data.json")

    with open(file_path) as file:
        data = json.load(file)

    test_tupple=[]

    for item in data:
        test_tupple.append((
            item["name"],
            item["email"],
            item["subject"],
            item["message"],
            item["expected_success"]
        ))

    return test_tupple