# Exercise 1: Basic Set Operations
a={10,20,30,"surbhi",True,1}

a.add(22)
print(a)
a.remove(1)
print(a)
a.discard("surbhi")
print(a)
# Exercise 2: Clear All Elements

a.clear()
print(a)
# Exercise 3: Find the Length of a Set
b={1,2,3}
print("lenght of the set is :",len(b))
# Exercise 4: Check if a Set is Empty
if len(b)==0:
    print("Set is empty")
else:
    print("Set is not empty")
# Exercise 5: Union of Sets

set1={1,2,3,3}
#print(set1)
set2 = {3,4,5,6}
union_set = set1|set2
print(union_set)
# Exercise 6: Intersection of Sets
intersection_Set = set1&set2
print(intersection_Set)
# Exercise 7: Difference of Sets
diffrence_set = set1-set2
print(diffrence_set)
# Exercise 8: Symmetric Difference
s1={1,2,3,5,True,"python"}
s2={1,2,3,"Surbhi"}
symmetric_diff = s1.symmetric_difference(s2)
print("symmetric diffrence is :", symmetric_diff)

# Exercise 9: Find Max and Min
set4 = {1,2,3,5,6,11,30}
print("maximum value in set :",max(set4))
print("Minimum value in set :",min(set4))

# Exercise 10: Sum of Set Elements
set3 = {1,2,3,4,5}
sum1=0
for i in set3:
    sum1+=i
    i+=1
print(sum1)
#Sum method
print("Sum of the set values :",sum(set3))



