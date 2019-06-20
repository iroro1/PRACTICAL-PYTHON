# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates. 
# Extras:  Write two different functions to do this - one using a loop and constructing a list, and another using sets. Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def duprem(l):
    rem = set(l)
    return list(rem)

def duprem2(l):
    a=[]
    for i in l:
        if i in a:
            continue
        else:
            a.append(i)
    return a

lis1 = [1,2,2,3,65,5,89,9,87,4,65]

print(duprem(lis1))
print(duprem2(lis1))
