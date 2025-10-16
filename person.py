class Person:
    def __init__(self, name):
        self.name = name
                          #THIS IS SHOWING INHERITANCE
    def introduction(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    pass

class Lecturer(Person):
    pass

p1 = Person("PIUS")
L1 = Lecturer("Mr.Mark, I lecture Computer Science")
S1 = Student("KUTOSI, I do Software Engineering")

p1.introduction()
L1.introduction()
S1.introduction()
