#1 A Program to ask user for Name and Age and print out message
# that tells them the year they will turn 100 years.
#2 Add a function to ask user for number and print out that many
#copies of the message above.
#3 Print out the copies on different lines
import datetime

name = input('Enter your name: ')
age = input('Enter your age: ')
num_of_msg = input('How many Messages do you want to see? : ')
num= int(num_of_msg)
age_from_100= 100-int(age)
today = datetime.datetime.now()
onth_year= today.year + age_from_100
message = f"{name}, you'll be 100 years in another {age_from_100} years precisely in {onth_year}"
for i in range(num):
    print(message)
