class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print("Your name is " + self.name + " You are " + self.age )
    
    def update_age(self,new_age):
        self.age = new_age
    
    def change_name(self, new_name):
        self.name = new_name

person1 = Person("Janani", "28")
person1.display_info()
person1.update_age("15")
person1.display_info()
person1.change_name("Jan")
person1.display_info()