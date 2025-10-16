class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        print(speed)
        print(color)
        print("the __init__ is called")

# Instantiate objects outside the class definition
ford = Car(200, "gray")
Hillux = Car(180, "blue")
audi = Car(300, "black")

print(ford.speed)
print(Hillux.color)

ford.speed = 300
print(ford.speed)
print(ford.color)





class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        print(speed)
        print(color)

# Instantiate objects outside the class definition
ford = Car(200, "gray")
Hillux = Car(180, "blue")
audi = Car(300, "black")

print(ford.speed)
print(Hillux.color)

ford.speed = 300
print(ford.speed)
print(ford.color)