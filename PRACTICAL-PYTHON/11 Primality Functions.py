# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). 

def divisors(numb):
    numbList = [e for e in range(1, numb+1)]
    return [x for x in numbList if numb % x ==0 ]


def prime(x):
    a = divisors(x)
    # print(a)
    if len(a) < 3:
        print (f"{x} is a prime number.")
    else:
        print (f"{x} is NOT a prime number.")

numb = input('Enter a number User to check its primality. :')
numb = int(numb)


prime(numb)