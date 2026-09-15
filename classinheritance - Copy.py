class A:
    a=20
class B(A):
    b=30
class C(B):
    c=40
obj=C()
print(obj.a)
print(obj.b)
print(obj.c)
print(C.a)
print(C.b)
print(C.c)