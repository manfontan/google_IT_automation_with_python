# while my_variable < 10:
#     print("Hello")
#     my_variable += 1
## This code give an error because my_variable is not defined

# The code below prints "Hello" 5 times
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1

# The code below prints the sum and product of numbers from 1 to 9
# Because x is not initialized to 1 for the second while loop the product will be 1
x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

product = 1
# x = 1 # This line should be uncommented to get the correct product
while x < 10:
    product *= x
    x += 1

print(sum, product)
