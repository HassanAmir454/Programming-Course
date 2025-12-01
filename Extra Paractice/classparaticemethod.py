# class LABStudent:
#     name: str    #Attributes
#     age: int
#     major: str
#     def Introduce(self):  #method: ask the object to do something
#         return f"Hi, I am {self.name}, {self.age} years old, majoring in {self.major}"
#     def study(self):
#         return f"{self.name} is now studying {self.major}"
# Hassan = LABStudent()   #hassan is object or instance of LABStident
# Hassan.name = "Hassan"
# Hassan.age = 20
# Hassan.major = "AI engineer"

# Zeeshan = LABStudent()
# Zeeshan.name = "Zeeshan"
# Zeeshan.age = 20
# Zeeshan.major = "ML Expert"

# print(Hassan.Introduce())
# print(Hassan.study())
# print(Zeeshan.Introduce())
# print(Zeeshan.study())

#########################################################################################

# Now the easy way above one is not good programming this takes twoo long think if you have to this for 3000 students

class LABStudent:
    def __init__(self, name , age , major):
        self.name = name 
        self.age = age
        self.major = major
    def Introduce(self):  #method: ask the object to do something
        return f"Hi, I am {self.name}, {self.age} years old, majoring in {self.major}"
    def study(self):
        return f"{self.name} is now studying {self.major}"
    
Hassan = LABStudent("Hassan", 20, "AI engineering")
Zeeshan = LABStudent("Hassan", 20, "ML engineering")

print(Hassan.Introduce())
print(Hassan.study())
print(Zeeshan.Introduce())
print(Zeeshan.study())

