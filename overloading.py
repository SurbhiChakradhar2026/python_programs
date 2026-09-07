class Cat:
    def Speak(self):
        print("meow")
class Dog():
    def Speak(self):
        print("woof")

animals = [Cat(),Dog()]
for animal in animals:
    animal.Speak()