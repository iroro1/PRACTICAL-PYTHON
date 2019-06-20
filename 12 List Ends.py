# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.

def rand():
    import random
    return random.sample(range(5, 25), 5)


a= rand()
print(a)
newList = [a[0],a[-1]]
print(newList)