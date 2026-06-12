count = 1
while count <= 5 :
    print ("hello")
    count += 1

print(count)

i = 1
while i <= 100:
    print("hello world" , i)
    i+=1

i = 5 
while i >= 1:
    print(i)
    i -= 1

print("loop ended")


# Qus1 print number from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

print("loop ended")

# Qus2 print number from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# Qus3 print the multiplication table of a number n
n = int(input("enter the number"))
i = 1
while i <= 10:
    print(n * i)
    i += 1 

# Qus4 print the element of the following list using the loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 81

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
    i += 1

# Break statement
i = 1
while i <= 5:
    print(i)
    if (i == 4):
        break
    i += 1

    print ("end of the loop")

i = 1
while i <= 10:
    if(i%3 == 0):
        i += 1
        continue
    print(i)
    i += 1
    
# for loops
nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val) 

tup = (1, 2, 3, 4, 5, 6, 7, 2)

for num in tup:
    print(num)

# Qus1 For loops
# Print the element of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in nums:
    print(el )