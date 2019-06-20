# Take two lists, say for example these two:  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,15]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]

unionList = []

for e in a:
    for i in b:
        if e == i:
            unionList.append(e)

unionList = set(unionList)
print(unionList)