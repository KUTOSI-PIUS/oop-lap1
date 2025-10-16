class Car:
    def __init__(self, speed, color):
        self._speed = speed   # Private attribute
        self._color = color   # Private attribute
        print(f"Speed: {speed}")
        print(f"Color: {color}")
        print("The __init__ method is called")

    # Setter for speed
    def set_speed(self, new_speed):
        self._speed = new_speed

    # Getter for speed
    def get_speed(self):
        return self._speed

    # Setter for color
    def set_color(self, new_color):
        self._color = new_color

    # Getter for color
    def get_color(self):
        return self._color


# Instantiate objects
ford = Car(200, "gray")
hillux = Car(180, "blue")
audi = Car(300, "black")

# Use setter to change speed
ford.set_speed(500)

# Use getter to access speed and color
print(f"Ford's speed: {ford.get_speed()}")     # Output: 500
print(f"Hillux's color: {hillux.get_color()}") # Output: blue

# Direct access (not recommended if using getters/setters)
ford._speed = 300
print(f"Ford's updated speed: {ford.get_speed()}")  # Output: 300
print(f"Ford's color: {ford.get_color()}")          # Output: gray