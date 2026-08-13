class Student:

    def __init__(self, name, marks):
        print(f"Adding new student and naming him/her: \"{name}\"")
        self.name = name
        self.marks = marks

    def get_name(self):
        return self.name

student1 = Student(name="Nolin", marks=84)
print(student1.name)
print(student1.marks)

name = student1.get_name()
print(name)