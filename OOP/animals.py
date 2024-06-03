#polymorphism

class Animal:
    def make_sound(self):
        pass

    def move(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("chirp")

    def move(self):
        print("The bird is flying")

    def eat(self):
        print("The bird is swallowing")

class Fish(Animal):
    def make_sound(self):
        print("click")

    def move(self):
        print("swim")

    def eat(self):
        print("The fish is swallowing water with food")

class Dog(Animal):
    def make_sound(self):
        print("Barking")

    def move(self):
        print("The dog is running")

    def eat(self):
        print("The dog is chewing")

class Humans(Animal):
    def make_sound(self):
        print("sing")

    def move(self):
        print("walk")

    def eat(self):
        print("chewing food")                    

