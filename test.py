from flask import Flask, render_template, redirect, request, abort, send_from_directory
from questions import Questions
import random

app = Flask(__name__)


# Testing a different approach by creating a Questions class

# @app.route('/')
# @app.route('/index')
def index():
    user = {'username': 'Kim'}
    return render_template('index.html', title='Home', user=user)


question_prompts = [
        'Which has never been a NYC subway line?\n(a) J\n(b) K\n(c) 9\n(d) Q\n\n',
        'Which borough is used in the moniker for the New York Yankees?\n(a) Queens\n (b) Bronx\n (c) Brooklyn\n (d) Manhattan\n\n',
        'What famous hotel has a secret train platform beneath it?\n (a) Waldorf Astoria\n (b) The Plaza\n (c) The Carlyle\n (d) Gramercy Park Hotel\n\n',
        'How many steps lead to the crown of the Statue of Liberty?\n (a) What\'s the Statue of Liberty?\n (b) 327\n (c) 973\n (d) Idk, no one goes there besides tourists.\n\n',
        'What famous NYC landmark was originally used as a burial ground?\n (a) Coney Island\n (b) Washington Square Park\n (c) Central Park\n (d) Central Perk\n\n',
        'Which island was used a hospital for criminals, sick, and mentally ill patients:\n (a) Rikers Island\n (b) Long Island\n (c) Staten Island\n (d) Roosevelt Island\n\n',
        'Which can tout being the longest subway line?\n (a) 7\n (b) A\n (c) S\n (d) D\n\n',
        'Which acronym is relevant to New York?\n (a) LGA\n (b) BQE\n (c) NDQ\n (d) All of the above\n\n'
        ]


questions = [
    Questions(question_prompts[0], 'b'),
    Questions(question_prompts[1], 'b'),
    Questions(question_prompts[2], 'a'),
    Questions(question_prompts[3], 'd'),
    Questions(question_prompts[4], 'b'),
    Questions(question_prompts[5], 'd'),
    Questions(question_prompts[6], 'b'),
    Questions(question_prompts[7], 'd')

]


# Randomize the questions
# Chooses a random number between 1 and 15 and sets to random_q variable
#     question_id = random.randint(0, len(questions)-1)
#     random_q = questions[question_id]

#  TODO: Still need to limit to 8 questions


# @app.route('/quiz-1')
def run_quiz(q_list):
    score = 0
    for question in q_list:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 3

    print('You got ' + str(score) + '/' + str(len(q_list) * 3) + ' points.')

    if score >= 0 and score <= 6:
        print('Fuggedaboutit! You are no New Yorker!')
    if score >= 7 and score <= 12:
        print('Not quite... but you\'re still better than Staten Island!')
    if score >= 13 and score <= 19:
        print('You\'re getting warmer than a subway car during the morning commute!')
    if score >= 20 and score <= 24:
        print('Start spreading the news! You\'re an official New Yorker!')


run_quiz(questions)

    #
    #
    # return render_template('quiz.html', title='Start Game', question=random_q['q'], choice1=random_q['c1'], choice2=random_q['c2'],
    #                        choice3=random_q['c3'], choice4=random_q['c4'], page=page+1, question_id=str(question_id))


# @app.route('/final')
# def end():
    # TODO: return render_template(, title='Final Score')
# if __name__ == "__main__":
#     app.run(debug=True)