# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# The topics that you need for this exercise combine lists, conditionals, and user input. There is a new concept of creating lists.There is an easy way to programmatically create lists of numbers in Python.To create a list of numbers from 2 to 10, just use the following code:  x = range(2, 11)Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10].

numb = input('Enter number : ')
numb = int(numb)
numbList = []
for e in range(1, numb+1):
    numbList.append(e)

divisors = [x for x in numbList if numb % x ==0 ]

print(divisors)