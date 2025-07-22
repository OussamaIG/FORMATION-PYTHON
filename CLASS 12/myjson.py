import json

data = [{"name" : "oussama", "surname" :"IG"},{"name" : "oussama", "surname" :"IG"} ]

#add/create a json file
with open("myfile.json" , "w") as f:
    json.dump(data, f, indent=4)

#load data from the json file, returns an array
with open("admins.json", "r") as f:
    array = json.load(f)

print(array)