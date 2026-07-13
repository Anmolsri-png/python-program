# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(5, 10)

# calc_sum(12, 17)


# calc_sum(2, 10)


# function definition
# def calc_sum(a, b):
#     return a + b
# sum = calc_sum(1, 3)#function call;argument
# print(sum)


# def print_hello():
#     print("hello")

# output = print_hello()
# print(output)#none value

#average of 3 numbers

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(98, 97, 97)

#Default parameter
# def cal_prod(a=22, b=2):
#     print(a * b)
#     return a * b
# cal_prod()

# Qus WAF to print the length of a list (list is the parameter)

# cities = ["delhi", "gurgaon", "noida", "pune", "chennai"]
# heroes = ["thor", "ironman", "caption america", "shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

#WAF to print the elements of a list in a single line.(list is the parameter)
# cities = ["delhi", "gurgaon", "noida", "pune", "chennai"]
# heroes = ["thor", "ironman", "caption america", "shaktiman"]

# # print(heroes[0], end=" ")
# print(heroes[1], end=" ")

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes) 
# print_list(cities)
# print()

#WAF to find the factorial of n.(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6)