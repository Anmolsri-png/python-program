# f = open("demo", "a")
# f.write("\n this is my gr")
# f .close()

# with open("demo", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo", "w") as f:
#     data = f.write("close the retro theme")

# import os
# os.remove("demo") 

# PRACTICS
# Qus create a new file "practics.txt" using python. Add the following data in it:

# with open("practics.txt", "w") as f:

#     f.write("Hi everyone \n we are learning fileI/O \n")
#     f.write("using python \n to become a good coder")

# with open("file.txt", "w") as f:
#     f.write("hello everyone \nwe are learning file I/O\nusing Java\nI like programming in Java")

# QUS WAF that replaca all occurrences of "Java" and "python" in above file

# with open("file.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "Python")
# print(new_data)

# import os
# os.remove("file.txt")

# with open("file.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing Java\nI like programming In Java")

# with open("file.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("file.txt", "w") as f:
#     f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("file.txt", "r") as f:
#           data = f.read()
#           if(data.find(word)):
#               print("found")
#           else:
#               print("not found")  

# check_for_word()


