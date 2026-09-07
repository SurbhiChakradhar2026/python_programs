#duplicate char in list 

lst = ['India','is','my','country']
str = "".join(lst)
print(str)

duplicate =[]
for char in str:
    if str.count(char)>1 and char not in duplicate:
        duplicate.append(char)
#print(duplicate)
#to print String
print(*duplicate)

#unique char in list
# lst2 = ["test"]
# str2 = "".join(lst2)

# unique =[]
# for char in str2:
#     if str2.count(char)==1 and char not in unique:
#         unique.append(char)
# #print(unique)
# #to print String
# print(unique)