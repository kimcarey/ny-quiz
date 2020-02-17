from flask import Flask, render_template, redirect, request, abort, send_from_directory
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kim'}
    return render_template('index.html', title='Home', user=user)


@app.route('/quiz') # Do I need GET or POST methods for this route?
def quiz():
    page = request.args.get('page', default=1, type=int) # to recall the state/what quiz # the user is on

    questions = [
        {
            'q': 'The ____ train has never been a NYC subway line:',
            'c1': 'J',
            'c2': 'K',
            'c3': '9',
            'c4': 'Q'
    },
        {
            'q': 'Which borough is used in the moniker for the New York Yankees?',
            'c1': 'Queens',
            'c2': 'Bronx',
            'c3': 'Brooklyn',
            'c4': 'Manhattan'
        },
        {
            'q': 'What famous hotel has a secret train platform beneath it?',
            'c1': 'Waldorf Astoria',
            'c2': 'The Plaza',
            'c3': 'The Carlyle',
            'c4': 'Gramercy Park Hotel'
        },
        {
            'q': 'There are how many steps to reach the crown of the Statue of Liberty?',
            'c1': 'What\'s the Statue of Liberty?',
            'c2': '327',
            'c3': '973',
            'c4': 'Idk, no one goes there besides tourists.'
        },
        {
            'q': 'What famous NYC landmark was originally used as a burial ground?',
            'c1': 'Coney Island',
            'c2': 'Washington Square Park',
            'c3': 'Central Park',
            'c4': 'Central Perk'
        },
        {
            'q': 'Which island was used a hospital for criminals, sick, and mentally ill patients:',
            'c1': 'Rikers Island',
            'c2': 'Long Island',
            'c3': 'Staten Island',
            'c4': 'Roosevelt Island'
        },
        {
            'q': 'Which can tout being the longest subway line?',
            'c1': '7',
            'c2': 'A',
            'c3': 'S',
            'c4': 'D'
        },
        {
            'q': 'Which acronym is relevant to New York?',
            'c1': 'LGA',
            'c2': 'BQE',
            'c3': 'NDQ',
            'c4': 'All of the above'
        },
        {
            'q': 'What was Citifield\'s original name before it was changed in 2006?',
            'c1': 'Shea Stadium',
            'c2': 'Mets Piazza',
            'c3': 'Seaver Stadium',
            'c4': 'Flushing Meadows Park'
        },
        {
            'q': 'What do you call the bread for your sandwich?',
            'c1': 'Hero',
            'c2': 'Sub',
            'c3': 'Hoagie',
            'c4': 'Grinder'
        },
        {
            'q': 'The award for the most ethnically diverse borough goes to:',
            'c1': 'Staten Island',
            'c2': 'Queens',
            'c3': 'Brooklyn',
            'c4': 'Bronx'
        },
        {
            'q': 'The RFK Bridge will forever and always be the: ',
            'c1': 'Triborough Bridge',
            'c2': 'George Washington Bridge',
            'c3': 'Tappan Zee Bridge',
            'c4': 'Brooklyn Bridge'
        },
        {
            'q': 'Have you ever walked the Brooklyn Bridge?',
            'c1': 'Yes',
            'c2': 'No',
            'c3': 'Thought about it once',
            'c4': 'Maybe next year'
        },
        {
            'q': 'Fill in the blank: Grand Central _______?',
            'c1': 'Station',
            'c2': 'Park',
            'c3': 'Junction',
            'c4': 'Terminal'
        },
        {
            'q': 'Cellino and Barnes are well-known:',
            'c1': 'Financiers',
            'c2': 'Personal injury attorneys',
            'c3': 'Circus ringleaders',
            'c4': 'Cross streets in Manhattan'
        }
    ]


    random_q = questions[0] # TODO: Make this random for a list longer than one item
    # random_q = random.choice(questions)



    # TODO: To advance to the next page. Need to convert questions into a form that will be submitted
    next_page = '/quiz?page=' + str(page + 1)



    return render_template('quiz.html', title='Start Game', question=random_q['q'], choice1=random_q['c1'], choice2=random_q['c2'],
                           choice3=random_q['c3'], choice4=random_q['c4'], page=page, next_page=next_page)


# @app.route('/final')
# def end():
    # TODO: return render_template(, title='Final Score')
if __name__ == "__main__":
    app.run(debug=True)