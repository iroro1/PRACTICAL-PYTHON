# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.

numb = input('Enter a number : ')

if int(numb) % 2 == 0 :
    if int(numb) % 4 != 0:
        print(f"You entered {numb} which is even")
    elif int(numb) % 4 == 0:
        print(f"{numb} is a multiple of 4")
elif int(numb) % 2 == 1:
    print(f"You entered {numb} which is odd")

