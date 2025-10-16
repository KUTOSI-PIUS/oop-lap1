

class Student:
    def __init__(self,name):
        self.name = name                #This is a public attribute
        self._gpa =5                    #This is a protected attribute
        self.__password = "1234"        #This is a private attribute
                                    
student1 = Student("Pius")
print(student1.name)
print(student1._gpa)
print(student1.__password)  

class Student:
    def __init__(self, name)