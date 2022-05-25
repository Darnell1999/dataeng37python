# class Dog:
#     animal_type = "canine"
#
#     def bark(self):
#         return f"Woof! I am a {self.animal_type}"
#
# fido = Dog() #instantiation = creating an INSTANCE of the class
# print(fido.animal_type)
# print(fido.bark())
#
# lassie = Dog()
# print(lassie.animal_type)
# print(lassie.bark())
#
# print(fido)
# print(type(fido))
#
# Dog.animal_type = "arachnid"
# Dog.legs = 8
#
# print(fido.legs)
# print(fido.animal_type)
# print(lassie.animal_type)
# print(fido.bark())

# class Dog:
#     def __init__(self, name, colour): #initialise
#         self.animal_type = "canine"
#         legs = 4
#         self.name = name
#         self.colour = colour
#
#     def bark(self):
#         return f"Woof! I am a {self.animal_type}"
#
# fido = Dog() #instantiation = creating an INSTANCE of the class
# print(fido.animal_type)
# print(fido.bark())
#
# lassie = Dog()
# print(lassie.animal_type)
# print(lassie.bark())
#
# print(fido)
# print(type(fido))
#
# Dog.animal_type = "arachnid"
# Dog.legs = 8
#
# print(fido.legs)
# print(fido.animal_type)
# print(lassie.animal_type)
# print(fido.bark())

# class Spartan:
#     def __init__(self, name, dob, passport_no):
#         self.name = name
#         self.dob = dob
#         self.passport_no = passport_no
#         self.role = "Trainee"
#
#     def intro(self):
#         return f"Hello, I am {self.name}, I was born {self.dob} and I am a {self.role}"
#
#
# Darnell = Spartan("Darnell", "21-12-1999", "NWK304243")
# print(Darnell.intro())

# class Car:
#     def __init__(self, make, model, top_speed):
#         self.make = make
#         self.model = model
#         self.top_speed = top_speed
#
#     def car_stuff(self):
#         return f"This car is a {self.make} make and the model is {self.model}. This car has a top speed of {self.top_speed}"
#
#
# Car1 = Car("BMW", "A class", "120mph")
# print(Car1.car_stuff())
#
#
# class CarSpeed:
#     def __init__(self, current, acceleration, brake):
#         self.current = int(current)
#         self.acceleration = int(acceleration)
#         self.brake = int(brake)
#         self.speed = 0

    #
    # def car_speed(self):
    #     return f"The car is currently going at {self.current} mph. It has accelerated to {self.current + self.acceleration}. It has now slowed down to" \
    #            f"{self.current - self.acceleration - self.brake}"


#     def car_accelerate(self, acceleration):
#         self.speed += acceleration
#         return self.speed
#
# # speed = CarSpeed(30, 50, 40)
# # print(speed.car_speed())
#
# high_speed = CarSpeed(30, 40, 50)
# high_speed.car_accelerate(20)
# print(high_speed)


# Pillars of OOP

# 1. Abstraction - Making things available
# 2. Encapsulation - Protecting the code from being tampered with

# Finish worksheet (done), finish car class, read pep 8, practice python today (done) , functionalise fizzbuzz (done)
# project Euler dot net


