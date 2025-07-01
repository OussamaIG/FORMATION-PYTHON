user = {"username": "sevree.education", "password": "XWQOIRJSKS"}

#list to dict
lst = [("name", "Oussama"), ("surname", "IG")]
dt = dict(lst)

#update values
user["username"] = "newsevree"

#add attribute
user["createdAT"] = "2022"

#membership
print("username" in user)

#length
print(len(user))

#delete a key
del user["createdAT"]

#unpacking
key, val = user.popitem()

#clear
user.clear()

user = {"username": "sevree.education", "password": "XWQOIRJSKS"}

#turn into list
lst_keys = list(user)
lst_values = list(user.values())
lst = lst_values + lst_keys

#turn into a set
values_set = set(user.values())

#turn into tuple
items_tuple = tuple(user.items())
print(items_tuple)
