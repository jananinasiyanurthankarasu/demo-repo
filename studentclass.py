class Student:
    def __init__(self, name , major, gpa, is_on_probation):
        self.a = name
        self.b = major
        self.c = gpa
        self.d = is_on_probation
    
student1 = Student("Janani", "mca", "9.0", "True")
student2 = Student("Raghu", "eee", "10.0", "no")

print(student1.a)
print(student2.d)