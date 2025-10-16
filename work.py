class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, score):
        self.grades.append(score)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Average: {self.average():.2f}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())


# 1. Create 3 students and add multiple grades
s1 = Student("Pius", 15)
s1.add_grade(90)
s1.add_grade(85)
s1.add_grade(92)

s2 = Student("Marvin", 16)
s2.add_grade(70)
s2.add_grade(75)
s2.add_grade(80)

s3 = Student("Tony", 15)
s3.add_grade(95)
s3.add_grade(88)
s3.add_grade(93)

# 2. Add them to a school
school = School("ST.JULIAN HIGH SCHOOL")
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

# 3. Print the student with the highest average
top = school.top_student()
print(f"Top Student: {top}")




coins = 100
coins = 100+500
print('I have', coins, 'coins')


