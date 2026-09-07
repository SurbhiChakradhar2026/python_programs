# # Program 49: Write a Python program to find sum of elements in list.

# lst = [1,2,3,6,7,8,9,10]
# sums = sum(lst)
# print(sums)
# # Program 50: Write a Python program to Multiply all numbers in the list.
# lst1= [1,2,3,4,5]
# multiply =1
# for i in lst1 : 
#     multiply=multiply*i
#     i+=1
# print(multiply)



# # Program 51: Write a Python program to find smallest number in a list.
# print(max(lst))
# # Program 52: Write a Python program to find largest number in a list.
# # Program 53: Write a Python program to find second largest number in a list.
# sortlst = sorted(lst)
# print(sortlst[1])


# # Program 54: Write a Python program to find N largest elements from a list.
# # Program 55: Write a Python program to print even numbers in a list.
# # Program 56: Write a Python program to print odd numbers in a List.
# # Program 57: Write a Python program to Remove empty List from List.
# # Sample list containing lists
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
# Using a list comprehension to remove empty lists
filtered_list = [i for i in list_of_lists if i]
# Print the filtered list
print("List after removing empty lists:", filtered_list)

# # Program 58: Write a Python program to Cloning or Copying a list.
# lst4= list.copy(lst)
# # Program 59: Write a Python program to Count occurrences of an element in a list
# lst2 = [1,2,3,3,4,4]
# lst3 = lst2.count(1)
# print(lst4)