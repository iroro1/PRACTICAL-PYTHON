# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def Fibonacci(x):
    ans = []
    a=0
    b=0
    result = 1
    for e in range(1,x+1):
        ans.append(result)
        a = b
        b = result
        result = a + b
    
    print(ans)

def user():
    numb = input('How many Fibonacci Numbers do you want?  __')
    numb = int(numb)
    Fibonacci(numb)

user()