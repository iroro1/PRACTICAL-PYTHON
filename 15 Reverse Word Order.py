# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(a[::2]) the 2 is the step
# def reverseWord(w):
#   return ' '.join(w.split()[::-1])

def reverse(s):
    s = s.split()
    new=[]
    i=0
    while i < len(s):
        i+=1
        new.append(s[-i])
    a = " ".join(new)
    print(a)

def user():
    sent = input('Enter a sentence to reverse: ')
    reverse(sent)

user()