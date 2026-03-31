class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class DogChild(Dog):
    def eat(self):
        print("Eating Chicken")
d=DogChild()
d.speak()
d.bark()
d.eat()