# from collections import Counter

# # Sample list
# data_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# # Count occurrences
# element_counts = Counter(data_list)

# # # Convert to a standard dictionary and print
# # print(dict(element_counts))

# from collections import Counter

# ctr = Counter("hello")
# print(ctr)
# ctr2 = Counter(["a","b","b"])
# print(ctr2)


from collections import Counter


str = 'aaabbbcccdd'
str2=Counter(str)
print(str2)
for i in str2:
    if str2[i]>1:
        print(i)

    
   
