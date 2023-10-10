

class Car:
    def __init__(self, type, wheels, age):
        self.type = type
        self.age = age
        self.wheels = wheels

    def printAll(self):
        print("Type: ", type, "\nAge: ", age, "\nWheels: ", wheels)

    def getAge(self):
        return self.age

    def getType(self):
        return self.type

    def getWheels(self):
        return self.wheels

myCars = []
index = 0
while True:
    option = int(input(" New Car | Look | Change Car | Exit\n"))
    if option == 1:
        type = input("What type of car is it: ")
        age = int(input("How old is the car: "))
        wheels = int(input("How many wheels does it have: "))
        myCars.insert(index, Car(type, wheels, age))
        index = index + 1
    elif option == 2:
        option2 = int(input("Which car do you want to look at: "))
        myCars[option2].printAll()
    else:
        break



