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

# class Student:
    
#     def __init__(self,fullname,marks):
#         self.name = fullname
#         print("adding new student in database")

# s1 = Student("anil")
# print(s1.name)

# s2 = Student("vikash")
# print(s2.name)


# class Student:
#     def __init__ (self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding new student in database")
# s1 = Student("anil", 32)
# print(s1.name, s1.marks)

# s2 = Student("vipin", 23)
# print(s2.name, s2.marks)

class Student:
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome Student", self.name)

    def get_marks(self):
        return self.marks
    

s1 = Student("karan", 43)
s1.welcome()
print(s1.get_marks())