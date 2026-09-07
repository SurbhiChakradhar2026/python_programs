#  Exercise 1: Basic Tuple Operations
# creating them, retrieving individual elements using index positions, and measuring their size using len()
a= (1,2,3,4,5,"surbhi",True,False)
print(a) #Print tuple
print(a[::-1]) #Reverse
print(a[5][2:7]) #Print r from Surbhi
print("lenght of the tuple is", len(a))


# Exercise 2: The Trailing Comma
b=(2,)
print(b)
print(type(b))
# Exercise 3: Tuple Repetition
repet = a*2
print(repet)

# Exercise 4: Tuple Concatenation
b=(1,2,3)
print(a+b)
# Exercise 5: Tuple Slicing
print(a[0:8])
print(a[:])


# Exercise 6: Tuple Reversal
print(a[::-1])
# Exercise 7: Counting
print(len(a))
print(len(b))
# Exercise 8: Tuple Unpacking
ab=(2,4,5,3)
a,b,c,d = ab
print(a)
print(b)
print(c)
print(d)
# Exercise9: The Swap Trick
t1=(1,2,3)
t2=(2,3,4)
t1,t2 = t2,t1
print(t1,t2)
# Exercise 10: Nested Tuple Access
t3= (1,2,3,(1,2,4),(3,4,5),(5,6,7))
print(t3[3][0])


