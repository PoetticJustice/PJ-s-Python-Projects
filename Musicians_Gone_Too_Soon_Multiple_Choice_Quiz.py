import random

from random import randint

import time

#greeting

print ("Welcome to my Musician Gone Too Soon Guessing Game!\n")

#Request input players names for output
print ('\n-----------------------------------------------------------------------------------------\n')

player1 = input('Enter your name Player#1: ')
player2 = input('Enter your name Player#2: ')

players = [player1,player2]

#Greet players by name and print customized greeting- need if else function to select player
print()
greeting1 = 'Hello, {}!'.format(player1)
greeting2 = 'Hello, {}!'.format(player2)

#Greeting to individual player

print(greeting1)
print(greeting2)

print()     

print("In this game we will attempt to guess the other player's favorite musicians gone too soon. Please use uppercase. Let's begin!")
print()

time.sleep(2)
###########################################################################
#                          SET THE SCORE TO ZERO                          #
###########################################################################

score1 = 0
score1 = int(score1)  #Convert the 0 into a number so we can add scores

score2 = 0
score2 = int(score2)

###########################################################################
#                           QUESTION 1a                                    #
###########################################################################

#Print questions with option for a input letter for an answer
print ('QUESTION 1a: Who was nicked-named the Lizard King? \n')
print ('A. Tom Petty')
print ('B. Jim Morrison')
print ('C. Kurt Cobain')
print ('')

Q1a_answer = "B"
Q1a_response= input('Your answer : ')

# If else loop for correcto or incorrect answer with score counted for each player
if (Q1a_response != Q1a_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1a_response + ' is correct!')
    score1 = score1 + 1

print ('Your current score is ' + str(score1) + ' out of 5')
print ('\n-----------------------------------------------------------------------------------------\n')
# 2 second break between questions
time.sleep(2)

###########################################################################
#                           QUESTION 2a                                    #
###########################################################################

print ('QUESTION 2a: Whose mother Afena was a Black Panther legend? \n')
print ('A. Prince')
print ('B. Curtis Mayfield')
print ('C. Tupac Shakur')
print ('')

Q2a_answer = "C"
Q2a_response= input('Your answer : ')

if (Q2a_response != Q2a_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Yes that is the answer! ' + Q2a_response + ' is correct!')
    score1 = score1 + 1

print ('Your current score is ' + str(score1) + ' out of 5')
print ('\n-----------------------------------------------------------------------------------------\n')

time.sleep(2)

###########################################################################
#                           QUESTION 3a                                    #
###########################################################################

print ('QUESTION 3a: Whose  mother was a background singer for Aretha Franklin? \n')
print ('A. Whitney Houston')
print ('B. Janis Joplin')
print ('C. Amy Winehouse')
print ('')

Q3a_answer = "A"
Q3a_response= input('Your answer : ')

if (Q3a_response != Q3a_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Excellent! ' + Q3a_response + ' is correct!')
    score1 = score1 + 1

print ('Your current score is ' + str(score1) + ' out of 5') 
print ('\n-----------------------------------------------------------------------------------------\n')
time.sleep(2)



###########################################################################
#                           QUESTION 4a                                    #
###########################################################################

print ('QUESTION 4a: Who came to an untimely end after an April Fools Day family squirmish? \n')
print ('A. Kurt Cobain')
print ('B. Tom Petty')
print ('C. Marvin Gaye')
print ('')

Q4a_answer = "C"
Q4a_response= input('Your answer : ')

if (Q4a_response != Q4a_answer):
    print ('Sorry, player1 that is incorrect!')
else:
    print ('Yes! ' + Q4a_response + ' is correct!')
    score1 = score1 + 1

print ('Your current score is ' + str(score1) + ' out of 5')
print ('\n-----------------------------------------------------------------------------------------\n')
time.sleep(2)

###########################################################################
#                           QUESTION 5a                                    #
###########################################################################

print ('QUESTION 5a: What rock legend has a tree dedicated to her in Haight Ashbury? \n')
print ('A. Janis Joplin')
print ('B. Dolores Oriodan')
print ('C. Whitney Houston')
print ('')

Q5a_answer = "A"
Q5a_response= input('Your answer : ')

if (Q5a_response != Q5a_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('You got it! ' + Q5a_response + ' is correct!')
    score1 = score1 + 1

print ('Player 1 your FINAL score is ' + str(score1) + ' out of 5')
print ('\n-----------------------------------------------------------------------------------------\n')

print()
time.sleep(2)
print()
print ('Player 2 it is your turn. We are going to see if you can guess Player 1 favorites.')
print() 
time.sleep(2)

###########################################################################
#                          SET THE SCORE TO ZERO                          #
###########################################################################

score1 = 0
score1 = int(score1)  #Convert the 0 into a number so we can add scores

score2 = 0
score2 = int(score2)

###########################################################################
#                           QUESTION 1b                                    #
###########################################################################

print ('QUESTION 1b: Who partied like it was 1999?? \n')
print ('A. Michael Jackson')
print ('B. Tupac Shakur')
print ('C. Prince')
print ('')

Q1b_answer = "C"
Q1b_response= input('Your answer : ')

if (Q1b_response != Q1b_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1b_response + ' is correct!')
    score2 = score2 + 1

print ('Your current score is ' + str(score2) + ' out of 5')
print ('\n-----------------------------------------------------------------------------------------\n')

time.sleep(2)

###########################################################################
#                           QUESTION 2b                                   #
###########################################################################

print ('QUESTION 2b: Whose ballads gave an nod to the Irish Republican Army? \n')
print ('A. Amy Winehouse')
print ('B. Whitney Houston')
print ('C. Dolores ORiordan')
print ('')

Q2b_answer = "C"
Q2b_response= input('Your answer : ')

if (Q2b_response != Q2b_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Yes that is the answer! ' + Q2b_response + ' is correct!')
    score2 = score2 + 1

print ('Your current score is ' + str(score2) + ' out of 5')
print ('\n-----------------------------------------------------------------------------------------\n')

time.sleep(2)

###########################################################################
#                           QUESTION 3b                                    #
###########################################################################

print ('QUESTION 3b: Who composed the Superfly film soundtrack? \n')
print ('A. Curtis Mayfield')
print ('B. Jim Morrison')
print ('C. Prince')
print ('')

Q3b_answer = "A"
Q3b_response= input('Your answer : ')

if (Q3b_response != Q3b_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Excellent! ' + Q3b_response + ' is correct!')
    score2 = score2 + 1

print ('Your current score is ' + str(score2) + ' out of 5') 
print()
print ('\n-----------------------------------------------------------------------------------------\n')

time.sleep(2)



###########################################################################
#                           QUESTION 4b                                    #
###########################################################################

print ('QUESTION 4b: Who co-starred in the film adaptation of The Wiz? \n')
print ('A. Marvin Gaye')
print ('B. Michael Jackson')
print ('C. Curtis Mayfield')
print ('')

Q4b_answer = "B"
Q4b_response= input('Your answer : ')

if (Q4b_response != Q4b_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Yes! ' + Q4b_response + ' is correct!')
    score2 = score2 + 1

print ('Your current score is ' + str(score2) + ' out of 5')
print ('\n-----------------------------------------------------------------------------------------\n')
time.sleep(2)

###########################################################################
#                           QUESTION 5b                                    #
###########################################################################

print ('QUESTION 5b: What grundge singer was inspired by John Lennon?  \n')
print ('A. Amy Winehouse')
print ('B. Dolores Oriodan')
print ('C. Kurt Cobain')
print ('')

Q5b_answer = "C"
Q5b_response= input('Your answer : ')

if (Q5b_response != Q5b_answer):
    print ('Sorry, that is incorrect!')
else:
    print ('You got it! ' + Q5b_response + ' is correct!')
    score2 = score2 + 1

print()
print ('Player 2 your FINAL score is ' + str(score2) + ' out of 5')
print()

time.sleep(2)

print()
#GOodby messages formatted to individual players using inputted names
goodbye1 = 'Thank you for playing our game. And remember,do not use drugs fam, seek help. :). Goodbye, {}!'.format(player1)
goodbye2 = 'Thank you for playing our game. Life can be short, so take good care of yourself. :). Goodbye, {}!'.format(player2)

#Goodbye to individual players
print ('\n-----------------------------------------------------------------------------------------\n')
print()
print(goodbye1)
print()
print(goodbye2)
print()

print ('That was fun. Have a good day!')

time.sleep(4)
#exit prompt
exit()

