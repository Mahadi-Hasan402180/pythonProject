# we know that here class and object
"""
class Student:
    roll = ""
    cgpa = ""
    name = ""


mahadi = Student()
mahadi.roll = 101
mahadi.cgpa = 3.84
mahadi.name = "Mahadi Hasan"
print(f" Name: {mahadi.name}, Roll: {mahadi.roll} , CGPA: {mahadi.cgpa}")

ahsan = Student()
ahsan.roll = 102
ahsan.cgpa = 3.80
ahsan.name = "ahsan Hasan"
print(f" Name: {ahsan.name}, Roll: {ahsan.roll} , CGPA: {ahsan.cgpa}")



# we know that here class and object and function
class Student:
    roll = ""
    cgpa = ""
    name = ""

    def SetValue(self, name,  roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

    def Disply(self):
        print(f" Name: {self.name}, Roll: {self.roll} , CGPA: {self.cgpa}")


mahadi = Student()
mahadi.SetValue("mahadi", 100042, 3.84)
mahadi.Disply()

ahsan = Student()
ahsan.SetValue("ahsan Habib", 100052, 3.81)
ahsan.Disply()


# use constructor , it can not call and object initialize kra jai ,value set kore dewa jai.
# orthat object k build korar somoy value gulo set kore dewa jai
class Student:

    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
    def Disply(self):
        print(f" Name: {self.name}, Roll: {self.roll} , CGPA: {self.cgpa}")

mahadi = Student("mahadi",1001,3.84)
mahadi.Disply()

ahsan = Student("ahsan Habib",1002,3.81)
ahsan.Disply()

"""

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def CalculateArea(self):
       print("Area = ", 0.5*self.height*self.base)

t1 = Triangle(10,20)
t1.CalculateArea()
t2 = Triangle(20,30)
t2.CalculateArea()



