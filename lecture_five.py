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
