# Program 65: Write a Python program to find all duplicate characters in string.

from collections import Counter
s= "Surbhi chakradhar"

count_ele = Counter(s)
count = 0
print(count_ele)
for key_1, value in count_ele.items():
    if value >1: 
        count+=1
        print(f"{key_1}")



dict1= {"E":3,"B":2,"C":1,"D":4}
print(sorted(dict1.keys()))
print(sorted(dict1.values()))

#Program 70: Write a Python program to convert key-values list to flat dictionary.
lst1= ["banana","orange","apple"]
lst = [1,2,3]
lst3=dict(zip(lst,lst1))
print(lst3)