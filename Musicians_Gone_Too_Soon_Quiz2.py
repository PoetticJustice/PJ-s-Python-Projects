import random

from random import randint

import time

# Defining Score variables 
x = 0
score = x

# Welcome message
print ("Welcome to The Musicans Gone Too Soon Guessing Game!\n")
print()
#Prompt players for their names
player1 = input('Enter your name Player#1:\n ')
time.sleep(1)
player2 = input('Enter your name Player#2:\n')
time.sleep(1)
#Format the inputed data
greeting1 = 'Hello, {}!'.format(player1)
greeting2 = 'Hello, {}!'.format(player2)
print()
#Greet players by name
print(greeting1)
print()
print(greeting2)
print()
#Prompt to begin playing
print("OK  " + (player1) + " lets begin")
print()
time.sleep(1)

#Funtion to record answers of first set of questions
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
print()
#Begin the quiz offer multiple choice options for input in a list
question1_prompts = [

     "Who was nicked-named the Lizard King?\na) Curtis Mayfield\nb) Prince\nc) Jim Morrison\nd) Tupac Shakur\n",
     "Who co-starred in the film adaptation of The Wiz?\na) Whitney Houston\nb) Michael Jackson\nc) Prince\nd) Marvin Gaye\n",
     "What rock legend has a tree dedicated to her in Haight Ashbury?\na) Janis Joplin\nb) Whitney Houston \nc) Dolores ORiordan \nd) Amy Winehouse\n",  
     "Who was known as a baby Bob Dylan?\na) Marvin Gaye \nb) Jim Morrison\nc) Tom Petty\nd) Kurt Cobain\n",
     "Who composed the Superfly film soundtrack?\na) Tupac Shakur\nb) Whitney Houston\nc) Prince\nd) Curtis Mayfield\n",
     "Whose ballads gave a nod to the Irish Republican Army?\na)Janis Joplin \nb) Jim Morrison \nc) Amy Winehouse \nd) Dolores ORiordan\n"
]  
#Multiple choice answers sorted into a list
questions1 = [
     Question(question1_prompts[0], "c"),
     Question(question1_prompts[1], "b"),
     Question(question1_prompts[2], "a"),
     Question(question1_prompts[3], "c"),
     Question(question1_prompts[4], "d"),    
     Question(question1_prompts[5], "d")
]
#Function to track score of each player
def run_quiz(questions1):
     score = 0
     for question1 in questions1:
          answer = input(question1.prompt)
          if answer == question1.answer:
               score += 1
     print("Congratulations!", player1, " you got", score, "out of", len(questions1))
print()
run_quiz(questions1)
print()
print()
print("OK  " + (player2) + " it's your turn. Let's begin")
time.sleep(1)
print()
##########Player 2 questions repeats the entire sequence

questions2 = {
    
    'Who partied like it was 1999?' : 'Prince',
    'What was the name of the artist who recorded Rehab?' : 'Amy Winehouse',
    'What grundge singer was inspired by John Lennon? ' : 'Kurt Cobain',
    'Whose mother Afena was a Black Panther legend?' : 'Tupac Shakur',
    'Whose  mother was a background singer for Aretha Franklin?' : 'Whitney Houston',
    'Who came to an untimely end after an April Fools Day family squirmish?' : 'Marvin Gaye'
    }

question2_prompts = [

     "Who partied like it was 1999?\na) Curtis Mayfield\nb) Prince\nc) Jim Morrison\nd) Tupac Shakur\n",
     "What was the name of the artist who recorded Rehab?\na) Whitney Houston\nb) Janis Joplin\nc) Curtis Mayfield\nd) Amy Winehouse\n",
     "What grunge singer was inspired by John Lennon?\na) Kurt Cobain\nb) Jim Morrison  \nc) Dolores ORiordan \nd) Tom Petty\n",  
     "Whose mother Afena was a Black Panther legend?\na) Marvin Gaye \nb) Tupac Shakur\nc) Whitney Houston\nd) Prince\n",
     "Whose  mother was a background singer for Aretha Franklin?\na) Michael Jackson\nb) Whitney Houston\nc) Prince\nd) Curtis Mayfield\n",
     "Who came to an untimely end after an April Fools Day family squirmish?\na) Marvin Gaye\nb) Jim Morrison \nc) Prince \nd) Michael Jackson\n"
]
     
questions2 = [
     Question(question2_prompts[0], "c"),
     Question(question2_prompts[1], "d"),
     Question(question2_prompts[2], "a"),
     Question(question2_prompts[3], "b"),
     Question(question2_prompts[4], "b"),    
     Question(question2_prompts[5], "a")
]

def run_quiz(questions2):
     score = 0
     for question2 in questions2:
          answer = input(question2.prompt)
          if answer == question2.answer:
               score += 1
     print("Congratulations!", player2, " you got", score, "out of", len(questions1))
print()
run_quiz(questions2)
print()
#Goodbye message and Exit prompt
print("That's the End! Remember that drugs are bad, and if you are in trouble seek help.\n Thanks for playing!")
print()
time.sleep(3)
quit()

