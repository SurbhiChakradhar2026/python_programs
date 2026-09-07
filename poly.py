class A:
    def m(self):
        print("method")

class B(A):
    def m(self):
        print("Method Overriding")

obj=B()
obj.m()
