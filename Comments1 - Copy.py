# # Exercise 1. Perform Basic List Operations
# # Access the third element of a list
# # lst= [1,2,3,4]
# # print(lst[2])
# # # List Length: Print the total number of items
# # print(len(lst))
# # # Check if the list is empty

# # if len(lst) == 0:
# #     print("empty list")
# # else:
# #     print("list is not empty")

# # Exercise 2. Perform List Manipulation

# # Change Element: Change the second element of a list to 200 and print the updated list.
lst= [10,20,40,60,99,55]
# # lst[1]=200
# # print(lst)
# # # Append Element: Add 600 o the end of a list and print the new list.
# # lst.append(600)
# # print(lst)
# # # Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
lst.insert(2,300)
print(lst)
# # # Remove Element (by value): Remove 600 from the list and print the list.
# # lst.remove(600)
# # # Remove Element (by index): Remove the element at index 0 from the list print the list.
# # lst.pop(0)
# # print(lst)



# # Exercise 3. Sum and Average of All Numbers in a List

# # sum=0
# # for i in lst: 
# #     sum+=i
# # print(sum)
# # Avg= sum/len(lst)
# # print(Avg)
# # print("Sum of total", sum(lst))
# # print("Avg of the list value is ", sum(lst)/len(lst))

# # # Exercise 4. Find Maximum and Minimum from List
# # print("max value from list is", max(lst))
# # print("minimum value from list is", min(lst))
# # # Exercise 5. Calculate the Product of All Elements
# # lst1 = [1,2,3]
# # product=1
# # for i in lst1:
# #     product=product*i
# # print(product)


    
# # Exercise 6. Count Even and Odd Numbers
# lst=[10,20,30,20,3,7,21]
# counteven=0
# countodd=0
# for i in lst:
#     if i%2==0:
#         counteven+=1
#     else:
#         countodd+=1
# print("Even count",counteven)
# print("Odd count",countodd)
# # Exercise 7. Reverse a List
# print(lst[::-1])
# # Exercise 8. Sort a List of Numbers
# sortlst= lst.sort()
# print(sortlst)
# # Exercise 9. Create a Copy of a List
# lst3=[1,2,4,3,5]
# lst2= lst3.copy()
# print(lst2)
# # Exercise 10. Combine Two Lists
# print(lst2+lst3)
