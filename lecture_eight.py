# class Student:
#     name = "Vipin"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

class Student:
    
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database")

s1 = Student("anil")
print(s1.name)

s2 = Student("vikash")
print(s2.name)