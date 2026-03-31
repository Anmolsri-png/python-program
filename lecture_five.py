while True :
    print("hello")

count = 1
while count <= 5 :
    print("hello")
    count += 1

print(count)

i = 1
while i <= 10:
    print("my skill", i)
    i += 1

print(i)

i = 5
while i < 6:
    print(i)
    i -= 1

              #Qus ans
# Qus- Print numbers from 1 to 100. 
i = 1
while i < 100:
    print(i)
    i += 1

print(i)

# Qus  Print numbers from 100 to 1
i = 100
while i >= 1: #stopping condition
    print(i)
    i -= 1
        
# Qus  Print the multiplication table of a number n.
n = int(input("enter the number")) 
i = 1
while i <= 10:
    print(n*i)
    i += 1

#Qus Print the elements of the following list using a loop: 
#   [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
heros = ["ironman", "superman", "thor", "batman", "captian"]
idx = 0
while idx < len(heros):
    print(heros[idx])
    idx += 1 

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1    

#Qus Search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81,100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16)
 
x = 16

i = 0 #initalization 
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding")
    i += 1

           ## Break and continue

i = 1
while i<=10:
    print(i)
    if(i == 7):
        break 
    i += 1

print("end of loop")

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25)
 
x = 25

i = 0       #initalization 
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding")
    i += 1

print("end of loop")

i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i+=1


veggi = ["brinjal", "potato", "ladyfinger", "cucumber", "tomato"]

for val in veggi:
    print(val)


tup = (2, 3, 4, 6, 8, 9)

for val in tup:
    print(val)

str = "my laptop"
for char in str:
    if(char == 'p'):
        print("found o")
        break
    print(char)
else:
    print("the end")
    
            #Qus ans
# Qus- using for
# Print the elements of the following list using a loop: 

nums = [1, 6, 4, 3, 90, 45, 34, 23, 89, 95, 100]
for el in nums:
    print(el)

# Qus- Search for a number x in this tuple using loop:

nums = (1, 6, 4, 3, 90, 45, 34, 23, 89, 95, 100,)
idx = 0
x = 90
for el in nums:
    if(el == x):
        print("number found at idx", idx)
   
    idx += 1

print(range(5))

seq = range(2, 11)  #range(start , stop)
for i in seq:
    print(i)


seq = range(2, 11, 2)  #range(start , stop, step)
for i in seq:
    print(i)