class A:
    s=20
    def m(self):
        print("Hello Python method")

print(A.s)
#A.m()

#object 
obj = A()
print(obj.s)
obj.m()