class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self. major = major
        self.gpa = gpa
        self. is_on_probation = is_on_probation
    
    def display_info(self):
        print("your name " + self.name + "your gpa " + self.gpa)

    def with_honors(self):
        if self.gpa > "3.9":
            return True
        else:
            return False
        
    def change_name(self,new_name):
        self.name = new_name
    
    def update_gpa(self,new_gpa):
        self.gpa = new_gpa

student1 = Student("Janani", "MCA", "3.8" , "is_on_probation")
print(student1.display_info())
    
student1.change_name("Raghu")
print(student1.name)

student1.update_gpa("3.4")
print(student1.gpa)

print(student1.with_honors())