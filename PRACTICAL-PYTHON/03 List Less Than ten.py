# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numb = input('Enter number : ')
numb = int(numb)

# newA=[]
# for e in a:
#     if e < 5:
#         newA.append(e)

newA =[e for e in a if e < numb]  #one liner
print(newA)