# Make a two-player Rock-Paper-Scissors game. Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
def play(x,y):
    if (x == 'Rock' or x == 'rock') and (y == 'Scissors' or y == 'scissors'):
        print(f"{x} wins")
    elif (x == 'Scissors' or x == 'scissors') and (y == 'Paper' or y == 'paper'):
        print(f"{x} wins")
    elif (x == 'Paper' or x == 'paper') and (y == 'Rock' or y == 'rock'):
        print(f"{x} wins")
    elif (y == 'Rock' or y == 'rock') and (x == 'Scissors' or x == 'scissors'):
        print(f"{y} wins")
    elif (y == 'Scissors' or y == 'scissors') and (x == 'Paper' or x == 'paper'):
        print(f"{y} wins")
    elif (y == 'Paper' or y == 'paper') and (x == 'Rock' or x == 'rock'):
        print(f"{y} wins")

player1 = input('Enter your name Player one : ')
player2 = input('Enter your name Player two : ')
player1 = str(player1)
player2 = str(player2)
print('Start Game of Rock Paper Scissors: \n')

playAgain = 'y'

while( playAgain == 'y'):
    play1 = input(f"{player1}: Rock,Paper or Scissors : ")
    play2 = input(f"{player2}: Rock,Paper or Scissors: ")
    play1 = str(play1)
    play2 = str(play2)

    play(play1,play2)
    playAgain= input('Play again? enter y for yes and n for no : ')
