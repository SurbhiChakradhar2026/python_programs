# Program 1: Write a Python program to print "Hello Python". 
print("Hello python")
# Program 2: Write a Python program to do arithmetical operations addition and division.
# num=int(input("Enter the number 1st number ="))
# num2=int(input("Enter the number 2nd number="))
# num3 = num+num2
# print(f"sum: {num} + {num2} = {num3}")
# print("addition of number 1st and 2nd is =", num3)
# div = num/num2
# print("divison of the number/number2 is",div)


# # Program 3: Write a Python program to find the area of a triangle.
# height = float(input("Enter the height of the triangle :")) 
# base = float(input("Enter the base of the triangle is :"))
# area_of_triangle = 0.5*height*base
# print(f"Area of triangle is = 0.5*{height}*{base} :",area_of_triangle)


# Program 4: Write a Python program to swap two variables. 
a=10
b=20
temp= a
a=b
b=temp
print(a,b)


# Program 5: Write a Python program to generate a random number. 
import random
print(random.randint(1,10))

# Program 6: Write a Python program to convert kilometers to miles.
#7Write a Python program to display calendar.
import calendar
month = int(input("enter the month you want calender :"))
year = int(input("enter the year : "))
cal = calendar.month(year,month)
print(cal)
            