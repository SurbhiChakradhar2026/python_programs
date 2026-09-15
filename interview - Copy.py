#reverse string without built in function
s= "Surbhi"
str= ""
for i in s:
    #print(i,end="")
    str=i+str #  i add hoga is taraf +str
print(str) 

#First non-repeating character of given string
from collections import Counter

str2= "swiss" # w 
str_count = Counter(str2)
print(str_count)


test = "india"
print(test[-1])
print(test[:-2])
print(test[::-1])
# combine 2 list
list1 = ["my","name"]
list2=["is", "john"]# output = my name is john

list3= list1+list2
print(' '.join(list3))

list1.extend(list2)
print(list1)
print(' '.join(list1))
#combine 2 list and convert into dictionary
list4= ['a','b','c']
list5= [1,2,3]
list3= dict(zip(list4,list5))
print(list3)
#2nd dict comphrension
dict2 = {list4[i] : list5[i] for i in range (len(list4))}
print(dict2)