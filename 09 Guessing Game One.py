# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

numGuess= 0
a = random.randint(1,9)
end= 1
while (end != 0) or (end != 0):
    guess = input('Guess a number : ')
    guess = int(guess)
    numGuess +=1

    if guess < a:
        print('You guessed too low')
    elif guess > a:
        print('You guessed too high')
    else:
        print('You got it Genuis!!!')
    
    ended = input('"Enter exit" to quit : ')
    if (str(ended) == 'exit') or (str(ended) == 'Exit') or (str(ended) == 'EXIT'):
        end= 0
        
print(f"You took {numGuess} guesse(s).")