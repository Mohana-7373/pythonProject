class car:
    someclassdummyvar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)

Carobj = car()
Carobj.sample_car_instance_method("hello")

Carobj2 = car()
Carobj2.sample_car_instance_method(3)

class Car:
    someclassdummyvar = "dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)

carobj = Car()
carobj.sample_car_instance_method("Hello again!")

carobj2 = Car()
carobj2.sample_car_instance_method(2)

#static method
class staticclass:
    @staticmethod
    def sample_static_method_addition(x,y):
        return x+y

    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y

staticobj = staticclass()
output_add = staticobj.sample_static_method_addition(2,3)
output_mul = staticobj.sample_static_method_multiplication(2,3)
print(output_add,output_mul)

#classmethod
class classmethod:
    @classmethod
    def class_method(cls):
        print("this is class method")

obj = classmethod()
obj.class_method()

#instance method
class animal:
    def __init__(self, species, gender):
        self.species = species
        self.gender  = gender
animalobj = animal("dog","male")
print(animalobj.gender)
print(animalobj.species)

#
class Car:
    def __init__(self, color, max_speed, accleration, tyre_friction, start_engine, current_speed):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.start_engine = False
        self.current_speed = current_speed
    def start_engine(self):
        self.start_engine = True
        print(self.start_engine)
    def stop_engine(self):
        self.start_engine = False
        print(self.start_engine)

carObj = Car("Black", 120, 10, 20, False, 60)
carObj.start_engine()
carObj.stop_engine()
carObj.start_engine()
