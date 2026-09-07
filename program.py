
# # Exercise 1: Basic Dictionary Operations
# a = {"Name": "Surbhi", "age": 30}
# print(a)
# a["location"] = "Ghaziabad"

# print(a)

# a["age"] = 26 
# print(a)

# del a["age"]
# print(a)



# # Exercise 2: Dictionary Operations
# #find dict is empty or not
# dict_1 = {"name" : "Surbhi",
#           "Subject": "python"}
# # Print Len 
# print("Lenght of the dict is :", len(dict_1))

# #Check
# if len(dict_1) == 0:
#     print("Dictionary is empty ")
# else:
#     print("Not Empty")

# # Exercise 8: Initialize Dictionary with Default Values

# # Exercise 3: Dictionary from Two Lists
# comb2 = dict(zip(lst,lst2))
# print(comb2)
# # Exercise 4: Clear Dictionary
# dict_3 = {"name":"Surbhi", "age":30}
# dict_3.clear()
# print(dict_3)
# print(dict_3)
# # Exercise 5: Merge Dictionaries
# c ={"name": "Sur", "location":"Noida"}
# c2= {"color": "blue", "flower": "Rose"}
# c3= {**c,**c2}
# print(c3)

# # Exercise 6: Access Nested Dictionary
# person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
# print(person["address"]["city"])
# # Exercise 7: Access ‘history’ Key From a Nested Dictionary
# student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
# print(student['grades']["history"])
# # Exercise 8: Initialize Dictionary with Default Values
lst = ["name", "color", "age"]
lst2= [1,2,3]
comb = dict.fromkeys(lst,lst2)
print(comb)

# # Exercise 9: Rename a Key of Dictionary
# d = {"name": "Alice","class":"First","address":"Ghaziabd"}
# d["Location"]=d.pop("address")
# print(d)
# # Exercise 10: Delete a List of Keys
# d5= {"name": "Alice","class":"First","address":"Ghaziabd"}
# lst4 = ["name","class"]
# for i in lst4:
#     d5.pop(i)
# print(d5)
# [8:12 pm, 28/7/2026] Rishi Uncodemy: person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
# [8:12 pm, 28/7/2026] Rishi Uncodemy: student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
