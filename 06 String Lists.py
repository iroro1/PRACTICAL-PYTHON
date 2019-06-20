# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

uString = input('Enter a Word to test for Palindrome : ')
uString= str(uString)
rvs = uString[ ::-1] #-1 is the step which is moving from the last index backwards 

if uString == rvs:
    print('Palindrome')
else:
    print('Not palindrome')
