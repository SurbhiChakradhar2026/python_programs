# Program 10: Write a Python program to swap two variables without temp variable.
# a=10
# b=20
# a,b=b,a
# print(a,b)
# # Program 11: Write a Python Program to Check if a Number is Positive, Negative or Zero.
# num=int(input("Enter the number ,needs to check"))
# if num==0:
#     print("Number is Zero")
# elif num>0:
#     print("Number is positive")
# else:
#     print("number is negative")
# Program 12: Write a Python Program to Check if a Number is Odd or Even.
# num1=int(input("enter number to be checked even or odd"))
# if num1%2==0:
#     print("number is even")
# # else:
#     print("number is odd")
# # Program 13: Write a Python Program to Check Leap Year.
# # year = int(input("enter the year to verify its leap year or not"))
# # if year%4==0 and year%100 !=0:
# #     print(f"{year} is Leap year")
# # elif year%100==0 and year%400 ==0:
# #     print(F"{year} IS Leap year")
# # else:
# #     print(f"{year}year is not leap year")
# # Program 14: Write a Python Program to Check Prime Number.

# num = int(input("Enter the number"))
# flag = False
# if num ==1:
#     print("Not Prime")
# elif num >1 :
#   for i in range(2,num) : 
#       if num%i==0:
#           flag = True
#           break
# if flag:
#     print(f"{num}, is not a prime number")
# else:
#     print(f"{num}, is a prime number")
    

# Program 15: Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
# # Program 16: Write a Python Program to Find the Factorial of a Number.

# fact_num = int(input("Enter the number = "))
# factorial =1

# if fact_num < 0:
#     print ("THis number doesnot have factorial")
# elif fact_num ==0:
#     print("factorial of number 0 is 1")
# else: 
#     for i in range(1,fact_num+1):
#         factorial = factorial*i
#     print(factorial)
        
# Program 17: Write a Python Program to Display the multiplication Table.
num = int(input("Enter the number :"))
for i in range(1,11):
    print(f"{num}*{i} = " , num*i)