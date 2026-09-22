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

# class Student:
#     college_name = "ABC college"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome Student", self.name)

#     def get_marks(self):
#         return self.marks
    

# s1 = Student("karan", 43)
# s1.welcome()
# print(s1.get_marks())


# x = int(input("enter your age?"))
# if 0<x<=5:
    
#     print("baby")
# else:
#     print("old")


# x = "awesome"

# def myfun():
#   print("Python is"  + x)
# myfun()

# print ("I am" ,25, "yeras old")




# a = int (input("Enter the number")) 
# b = int (input("Enter the number"))
# if b > a :
#     print ("False")
# else:
#     print("True")


# for n in range(1,9): 
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()      

# print("Please Enter Your Marks to Calculate Your Grade")
# Math = int (input("Enter Math Marks out of 100: "))
# Science = int (input("Enter Science Marks out of 100: "))
# Bio = int (input("Enter Bio Marks out of 100: "))
# print("Math: ", Math, "| Science: ",Science, " | Bio: ", Bio )
# sum = Math + Science + Bio
# print("Student Total Marks out of 300: ", sum)
# a = (sum / 300)*100 
# print("Percent: ",a)
# if a > 60:
#     print("Grade A")

# elif a < 60 and a > 50:
#     print("Grade B")
# elif a < 50 and a > 35:
#     print("Grade C")
# else:
#     print("fail")


# a = 33
# b= 2

# print(a%b)
# print(a/b)


# Math =40
# Bio = 40
# Science= 40

# sum = Math+ Bio+ Science
# print(sum)
# n = (sum/300)*100
# print(n)
# if n >= 70:
#     print("Grade A")
# elif n < 70 and n >=40:
#     print("Grade B")

# elif n < 30 and n > 20:
#     print("Grade C")

# else:
#     print("Fail")




# num = int(input("Enter the number"))
# if num <= 1:
#     print("Not a Prime number")
# else:
#     for i in range (2,num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")


# n = 5 

# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
   



n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)




# txt = "Hello, World!"
# print(txt[2:5])
# a = "Hello,World!"
# print(a.upper())
# name = "Python"
# print(f"I love {name}")

def myfunction():
    return True

if myfunction():
    print("True")
else:
    print("True")


# The count variable is assigned in the IF statement, and given the values 5
# Using Walrus operator
number =[1,2,3,4,5]

if (count :=len(number)) > 3:
    print(f"List has {count} element")