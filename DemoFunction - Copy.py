# def m(a,b):
#     print("Hello Python Function",a, b)
#     print(a+b)

# m(90,20)
# m(1,3)
# m(1.1,2.1)

# # WAP to define a function for sum, difference, multiplication and division
# def sum(x,y):
#     print("Sum of the values",x+y)
# sum(1,2)
# def difference(a,b):
#     print(a-b)
# difference(5,3)

# def multiply(a,b):
#     print(a*b)
# multiply(2,3)

# def division(a,b):
#     print(a/b)
# division(25,5)
# # WAP to print the even number from a range by defining functions
# def even(num):
#     for i in range(0,num+1):
#         if i%2 == 0:
#             print(i)
# even(20)
# # 1. Write a Python function to find the maximum of three numbers.
# def max3(a,b,c):
#     if a>b and a>c:
#         print (f"{a} is Max")
#     elif b>a and b>c:
#         print(f"{b} is Max")
#     else:
#         print(f"{c} is greater")
# max3(10,20,30)
# 2. Write a Python function to sum all the numbers in a list.
def sum_lst(num):
    print(sum(num))
sum_lst([1,2,3])

   

# 3. Write a Python function to multiply all the numbers in a list.

def lst_muliply(list1):
    start =1
    for i in list1:
        start=start*i
    print(start)
lst_muliply([1,2,3])


# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
def cal_fact(num):
    if num ==0:
        print("zero factorial is 1")
    elif num<0:
        print("Negative number does not have factorial")
    else:
        i=1
        m=1
        for i in range(1,num+1):
            m=m*i
        print(m)
cal_fact(5)
cal_fact(0)
cal_fact(1)
cal_fact(-1)
# 5. Write a Python program to print the even numbers from a given list.

def list_even(num):
    for i in num:
        if i%2==0:
            print(i)
        else:
            print("odd")
list_even([1,2,3,4,6])
