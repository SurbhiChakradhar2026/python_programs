# def is_palindrome(s):
#     if s == s[::-1]:
#         print("palindrom")
#     else:
#         print("not palindrom")
# is_palindrome("121")

# Problem 2:

# Automation testers often need to compare 
# test data — e.g., checking if two API responses (as lists) contain the same elements, regardless of order.

# Write a function same_elements(list1, list2) 
# that returns True if both lists contain exactly the same elements (same counts), regardless of order.
# from collections import Counter
# def same_elements(list1,list2):
#   #  return sorted(list1)==sorted(list2)
#      return Counter(list1)==Counter(list2)

# print(same_elements([1,2,3],[1,2,3]))
# print(same_elements([1,2],[1,2,3]))
# print(Counter([1,2,3]))


# from email_validator import validate_email
# def is_valid_email(email):
#     return validate_email(email)
# is_valid_email("test@example.com")   # True
# is_valid_email("test@@example.com")  # False
# is_valid_email("test example.com")   # False
# is_valid_email("test@examplecom")    # False



'''import keyword
print("The list of keywords are : ")
print(keyword.kwlist)'''

