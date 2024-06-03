#Inheritance of classes

class  Vehicle:
    def __init__ (self,make,model,color):
        self.make = make 
        self.model = model
        self.color = color

        def move(self):
            print("starts moving")

        def hoot(self):
            print("Honk honk")

class Bus(Vehicle):
    def __init__ (self,make,model,color,capacity):
        super().__init__ (make,model,color)
        self.capacity = capacity

        def __init__ (self):
            print("The bus is now boarding")

class Lorry(Vehicle):
    def __init__ (self,model,make,color,max_load):
        super().__init__ (make,model,color)
        self.max_load = max_load

        def __init__ (self):
            print("started loading")  
        def __init__ (self):
            print("finished offloading")                           