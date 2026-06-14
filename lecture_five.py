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

for i in range(2, 10):
    print(i)

for i in range(2, 10, 2):
    print(i)

for i in  range(2, 100, 2):
    print(i)

#Qus1 print numbers from 1 to 100
for i in range(1, 101):
    print(i)

#Qus print numbers from 100 to 1
for i in range(101, 0, -2):
    print(i)

#Qus print the multiplication table of a number n.
n = int(input("enter the number:"))
for i in range(1, 11):
    print(n * i)
    
# pass statement
for i in range(5):
    pass

print("some useless work")

#Qus WAP to find the sum of first n numbers (using while)
n = 6
sum = 0
i = 1
while i <= n:
    sum += i
for i in range(1, n+1):
    sum += i
    i += 1
print("total sum",sum)

#Qus WAP to find ftorial of first n numbers (using for)
n = 5
fact = 1
i = 1 
while i <= n:
    fact *= i 
    i += 1
    print("factorial=", fact)