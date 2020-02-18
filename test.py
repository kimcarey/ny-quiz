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
        'Which has never been a NYC subway line?\n (a) J\n (b) K\n (c) 9\n (d) Q\n\n',
        'Which borough is used in the moniker for the New York Yankees?\n (a) Queens\n (b) Bronx\n (c) Brooklyn\n (d) Manhattan\n\n',
        'What famous hotel has a secret train platform beneath it?\n (a) Waldorf Astoria\n (b) The Plaza\n (c) The Carlyle\n (d) Gramercy Park Hotel\n\n',
        'How many steps lead to the crown of the Statue of Liberty?\n (a) What\'s the Statue of Liberty?\n (b) 327\n (c) 973\n (d) Idk, no one goes there besides tourists.\n\n',
        'What famous NYC landmark was originally used as a burial ground?\n (a) Central Perk\n (b) Washington Square Park\n (c) Central Park\n (d) Coney Island\n\n',
        'Which island was used a hospital for criminals, sick, and mentally ill patients:\n (a) Rikers Island\n (b) Long Island\n (c) Staten Island\n (d) Roosevelt Island\n\n',
        'Which subway line can tout being the longest?\n (a) 7\n (b) A\n (c) S\n (d) D\n\n',
        'Which acronym is relevant to New York?\n (a) LGA\n (b) BQE\n (c) NDQ\n (d) All of the above\n\n',
        'What was Citifield\'s original name before it was changed in 2006?\n (a) Shea Stadium\n (b) Mets Piazza\n (c) Seaver Stadium\n (d) Flushing Meadows Park\n\n',
        'What do you call the bread for your sandwich?\n (a) Hero\n (b) Sub\n (c) Hoagie\n (d) Grinder\n\n',
        'The award for the most ethnically diverse borough goes to:\n (a) Staten Island\n (b) Queens\n (c) Brooklyn\n (d) Bronx\n\n',
        'The RFK Bridge will forever and always be the:\n (a) Tappan Zee Bride\n (b) Brooklyn Bridge\n (c) Triborough Bridge\n (d) George Washington Bridge\n\n',
        'Have you ever walked the Brooklyn Bridge?\n (a) Yes\n (b) No\n (c) Thought about it once\n (d) Maybe next year\n\n',
        'Fill in the blank: Grand Central _______\n (a) Station\n (b) Park\n (c) Junction\n (d) Terminal\n\n',
        'Cellino and Barnes are well-known:\n (a) Financiers\n (b) Personal injury attorneys\n (c) Circus ringleaders\n (d) Cross streets in Manhattan\n\n'
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
questions_random = random.sample(questions, len(questions))


# @app.route('/quiz-1')
def run_quiz(q_list):
    score = 0
    counter = 0

    # Limit to a total of 8 questions
    if counter < 7:
        for question in q_list:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 3
            counter += 1

        print('You got ' + str(score) + '/' + str(len(q_list) * 3) + ' points.')

        if score >= 0 and score <= 6:
            print('Fuggedaboutit! You are no New Yorker!')
        if score >= 7 and score <= 12:
            print('Not quite... but you\'re still better than Staten Island!')
        if score >= 13 and score <= 19:
            print('You\'re getting warmer than a subway car during the morning commute!')
        if score >= 20 and score <= 24:
            print('Start spreading the news! You\'re an official New Yorker!')


run_quiz(questions_random)

    #
    #
    # return render_template('quiz.html', title='Start Game', question=random_q['q'], choice1=random_q['c1'], choice2=random_q['c2'],
    #                        choice3=random_q['c3'], choice4=random_q['c4'], page=page+1, question_id=str(question_id))


# @app.route('/final')
# def end():
    # TODO: return render_template(, title='Final Score')
# if __name__ == "__main__":
#     app.run(debug=True)