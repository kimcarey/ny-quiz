from flask import Flask, render_template, redirect, request, abort, send_from_directory
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kim'}
    return render_template('index.html', title='Home', user=user)


@app.route('/quiz')
def quiz():
    page = request.args.get('page', default=-1, type=int) # to recall the state/what quiz # the user is on
    page += 1
    question_id = request.args.get('question_id', type=int) # recall what random question was given.
    seed = request.args.get('seed', type=int, default=random.randint(0, 2048))
    answer = request.args.get('answer', type=str)
    # Keeping track of all of the user's responses.
    answers = request.args.get('answers', type=str, default="")

    # Convert our answers list in the url back to a list of strings.
    # Python splitting an empty string with a parameter, gives back a list w/ one empty string.
    # See https://stackoverflow.com/questions/16645083/when-splitting-an-empty-string-in-python-why-does-split-return-an-empty-list/16645307
    if answers:
        answers = answers.split(".")
    else:
        answers = []

    # If there is an answer, add it to the list of answers we're tracking so we can grade them at the end.
    if answer:
        answers.append(answer)

    questions = [
        {
            'q': 'Which has never been a NYC subway line?',
            'c1': 'J',
            'c2': 'K',
            'c3': '9',
            'c4': 'Q',
            'ans': 'c2'
    },
        {
            'q': 'Which borough is used in the moniker for the New York Yankees?',
            'c1': 'Queens',
            'c2': 'Bronx',
            'c3': 'Brooklyn',
            'c4': 'Manhattan',
            'ans': 'c2'
        },
        {
            'q': 'What famous hotel has a secret train platform beneath it?',
            'c1': 'Waldorf Astoria',
            'c2': 'The Plaza',
            'c3': 'The Carlyle',
            'c4': 'Gramercy Park Hotel',
            'ans': 'c1'
        },
        {
            'q': 'How many steps lead to the crown of the Statue of Liberty?',
            'c1': 'What\'s the Statue of Liberty?',
            'c2': '327',
            'c3': '973',
            'c4': 'Idk, no one goes there besides tourists.',
            'ans': 'c4'
        },
        {
            'q': 'What famous NYC landmark was originally used as a burial ground?',
            'c1': 'Central Perk',
            'c2': 'Washington Square Park',
            'c3': 'Central Park',
            'c4': 'Coney Island',
            'ans': 'c2'
        },
        {
            'q': 'Which island was used a hospital for criminals, sick, and mentally ill patients:',
            'c1': 'Rikers Island',
            'c2': 'Long Island',
            'c3': 'Staten Island',
            'c4': 'Roosevelt Island',
            'ans': 'c4'
        },
        {
            'q': 'Which can tout being the longest subway line?',
            'c1': '7',
            'c2': 'A',
            'c3': 'S',
            'c4': 'D',
            'ans': 'c2'
        },
        {
            'q': 'Which acronym is relevant to New York?',
            'c1': 'LGA',
            'c2': 'BQE',
            'c3': 'NDQ',
            'c4': 'All of the above',
            'ans': 'c4'
        },
        {
            'q': 'What was Citifield\'s original name before it was changed in 2006?',
            'c1': 'Shea Stadium',
            'c2': 'Mets Piazza',
            'c3': 'Seaver Stadium',
            'c4': 'Flushing Meadows Park',
            'ans': 'c1'
        },
        {
            'q': 'What do you call the bread for your sandwich?',
            'c1': 'Hero',
            'c2': 'Sub',
            'c3': 'Hoagie',
            'c4': 'Wedge',
            'ans': 'c1'
        },
        {
            'q': 'The award for the most ethnically diverse borough goes to:',
            'c1': 'Staten Island',
            'c2': 'Queens',
            'c3': 'Brooklyn',
            'c4': 'Bronx',
            'ans': 'c2'
        },
        {
            'q': 'The RFK Bridge will forever and always be the: ',
            'c1': 'Triborough Bridge',
            'c2': 'George Washington Bridge',
            'c3': 'Tappan Zee Bridge',
            'c4': 'Brooklyn Bridge',
            'ans': 'c1'
        },
        {
            'q': 'Have you ever walked the Brooklyn Bridge?',
            'c1': 'Yes',
            'c2': 'No',
            'c3': 'Thought about it once',
            'c4': 'Maybe next year',
            'ans': 'c1'
        },
        {
            'q': 'Fill in the blank: Grand Central _______?',
            'c1': 'Station',
            'c2': 'Park',
            'c3': 'Junction',
            'c4': 'Terminal',
            'ans': 'c4'
        },
        {
            'q': 'Cellino and Barnes are well-known:',
            'c1': 'Financiers',
            'c2': 'Personal injury attorneys',
            'c3': 'Circus ringleaders',
            'c4': 'Cross streets in Manhattan',
            'ans': 'c2'
        }
    ]

    # Check if we should stop giving questions and grade the quiz.
    if page >= 8:
        random.seed(seed)
        questions_asked = random.sample(questions, k=8)
        score = 0
        message = ""
        for i, q in enumerate(questions_asked):
            correct = (q['ans'] == answers[i])
            if correct:
                score += 3
        if score >= 0 and score <= 6:
            message = 'Fuggedaboutit! You are no New Yorker!'
        if score >= 7 and score <= 12:
            message = 'Not quite... but you\'re still better than Staten Island!'
        if score >= 13 and score <= 19:
            message = 'You\'re getting warmer than a subway car during the morning commute!'
        if score >= 20 and score <= 24:
            message = 'Start spreading the news... You\'re an official New Yorker!'
        return render_template('results.html', title='Results', score=score, message=message, total=3*8)

    ### MAKE NEW PAGE

    # Randomize the questions
    # Chooses a random number between 1 and 15 and sets to random_q variable
    next_question_id = get_next_question_index(page, seed, len(questions))
    next_random_q = questions[next_question_id]

    # Encode our list of answers into a single string with period as the separator.
    # This is only so the URL looks nicer really.. (avoids lots of %28 like chars)
    answers = ".".join(answers)

    return render_template('quiz.html', title='Start Game', question=next_random_q['q'],
                           c1=next_random_q['c1'], c2=next_random_q['c2'],
                           c3=next_random_q['c3'], c4=next_random_q['c4'],
                           page=page, question_id=str(next_question_id),
                           seed=seed, answers=answers)



def get_next_question_index(page, seed, total_questions):
    random.seed(seed)
    idx_list = random.sample(range(total_questions), k=8)
    return idx_list[page]


if __name__ == "__main__":
    app.run(debug=True)