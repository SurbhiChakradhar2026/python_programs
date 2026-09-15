# Write a Python program to find the maximum of three numbers

num = int(input("Enter the First number ="))
num2= int(input("Enter the Second number ="))
num3= int(input("Enter the Third number="))
if num>num2 and num>num3:
    print("First number is the Maximum number")
elif num2>num and num2>num3:
    print("Second number is the Maximum number")
else:
    print("Third number is the Maximum number")

