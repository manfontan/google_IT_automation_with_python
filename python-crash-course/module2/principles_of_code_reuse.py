name =  "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name =  "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

# The code above is repetitive. We can use a function to avoid repetition.
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")