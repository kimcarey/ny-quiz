import time
import random

# list of questions
# TODO: Use random.choice to randomize the list
#TODO: Should this be a dict so that I can attach the correct answer? How do you randomize a dict?
questions = [
    'placeholder question 1?',
    'placeholder question 2?',
    'placeholder question 3?',
    'placeholder question 4?',
    'placeholder question 5?',
    'placeholder question 6?',
    'placeholder question 7?',
    'placeholder question 8?',
    'placeholder question 9?',
    'placeholder question 10?',
    'placeholder question 11?',
    'placeholder question 12?',
    'placeholder question 13?',
    'placeholder question 14?',
    'placeholder question 15?'
]



# game set up
print('So you think you\'re a real New Yorker?')
time.sleep(2)
print('Take this quiz to find out.')
time.sleep(2)
print('You\'ll be given 8 chances to prove it.')
time.sleep(2)
print('Are you ready?')
time.sleep(2)
print('Begin...\n')
time.sleep(2)


# keep track of score
score = 0

# Ask the question
# TODO: Will this need to be a loop? Need to ensure it only asks 8x
print('Question: ', random.choice(questions))
time.sleep(2)
print('a) lorem ipsum, b) loren ipsum, c) loren ipsum, d) lorem ipsum')
time.sleep(2)
answer = input('Enter your answer: ').lower()

# Evaluates player's answer and increment score if correct
if answer: #TODO: add code to check if answer is correct
    score += 3
    print('Correct!')
else:
    score += 0
    print('Wrong Answer!')


# Determine final score


# Deliver final message
if score >= 0 and score <= 6:
    print('Fuggedaboutit! You are no New Yorker!')
if score >= 7 and score <= 12:
    print('Not quite... but you\'re still better than Staten Island!')
if score >= 13 and score <= 19:
    print('You\'re getting warmer than a subway car during the morning commute!')
if score >= 20 and score <= 24:
    print('Start spreading the news! You are an official New Yorker!')


# Ask the player if they want to play again
