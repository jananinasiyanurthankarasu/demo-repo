class Person:
    def __init__(self, name, age):
        self.a = name
        self.b = age
    
    def display_info(self):
        print("name " + self.a + "," "age " + self.b )
    

person1 = Person("Janani", "28")
person1.display_info()