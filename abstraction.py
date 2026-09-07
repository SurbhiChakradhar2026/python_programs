from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def Speak(Self):
        pass
class Dog (Animal):
    def Speak(self):
        print("woof")
dog =Dog()
dog.Speak()