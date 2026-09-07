a = lambda x,y :print(x+y)
a(2,3)

# Write a Python program to sort tuples using Lambda.
sort_tup = lambda num : print(sorted(num))

sort_tup((9,6,3,2,1,8))
# Write a Python program to square and cube every number in a given list of integers using Lambda
num = [1,2,3,5]
Square = list(map(lambda d : d**2,num))
cube = list(map(lambda d: d**3,num))
print(Square)
print(cube)
# Write a Python program to count the even and odd numbers in a given list of integers using Lambda.
count_even = list(filter(lambda i : i%2==0,num))
print("number is even", count_even)
count_odd = list(filter(lambda i : i%2!=0, num))
print("number is odd",count_odd)
# Write a Python program to add two given lists using map and lambda.
l=[1,2,3]
l2=[2,3,4]
lst_add = list(map(lambda a,b : a+b,  l, l2 ))
print(lst_add)
