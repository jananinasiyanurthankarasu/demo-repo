class student:
    def __init__(self, a, b, c, d):
        self.name = a
        self.major = b
        self.gpa = c
        self.is_on_probation = d

student1 = student("Janani","cs", 9.0,"f")
student2 = student("Raghu","eee", "10.0", "t")
print(student1.name)
print(student2.name)
# print(student2.gpa)
# print(student2.is_on_probation)
