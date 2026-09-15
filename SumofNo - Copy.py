#Exercise 2: Calculate sum of all numbers from 1 to a given number
num=int(input("enter the number = "))
i=1
count=0
while i <=num:
   
   count+=i
   i+=1
print(count)

#Exercise 3: Print multiplication table of a given number
num=int(input("enter the number"))
i=0
while i<=9:
   i+=1
   print(i*num)


#Exercise 4: Display numbers from a string using a loop
#Exercise 5: Count the total number of digits in a number

num = int(input("enter the number"))
count =0
while num !=0:
   count+=1
   num=num//10
print(count)
