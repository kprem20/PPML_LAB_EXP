class Animal:
    def Speak(self):
        print("Animal is speaking ")
class dog (Animal):
    def bark (self):
        print("Dog is barking ")
d=dog()
d.bark()
d.Speak()