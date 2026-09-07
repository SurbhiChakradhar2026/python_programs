class Animal:
    def speak(self):
        print("Animal Speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
dog =Dog()
dog.speak()
#a=Animal()
#a.speak()