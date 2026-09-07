class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a+b)
        print(self.a,self.b)
        #print(a,b)
a = A(1,2)