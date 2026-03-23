info = {
    "name" : "desktop",
    "subject" : ["python", "c++", "java"],
    "topic" : ("dir", "set"), 
    "age" : 45,
    "is adult" : True,
    "marks" : 90.9
}

print(info["subject"])
print(info["topic"]) 
print(info["marks"])  


             # Dictionary method

student = {
    "name" : "Anmol Srivastava",
    "subject" : {
        "phy", "math", "che",
    }
}

student.update({"city" : "delhi"})

print(student)

        # set

collection = {1, 2, 3, 2, 3, 4, "Hi", "connection"}

print(collection)
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("connection")
collection.add((1, 2, 3, 4))

collection.clear()
print(len(collection))



level = {"hello", "connection", "world", "coding", "python"}

print(level.pop())
print(level.pop())
print(level.pop())



value1 = {6, 9, 3}
value2 = {9, 3, 6}

print(value1.intersection(value2))

             #Qus ans

dic = {"table" : ["a piece of firniture" , "list of fact and figuare"],
        "cat" : "a small animal",
       
}

print(dic)

               #Qus ans

classroom = {
    "python", "java", "c++",
    "python", "javascript", "java",
    "python", "java", "c++", "c",
}
print(len(classroom))

            #Qus ans

marks = {}

x = int(input("enter physics : "))
marks.update({"physics" : x})

x = int(input("enter maths : "))
marks.update({"maths" : x})

x = int(input("enter che : "))
marks.update({"che" : x})

print(marks)

         # Qus ans

value = {
    "float" : 9.0,
    "int" : 9
}

print(value)