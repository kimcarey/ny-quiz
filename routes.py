from flask import Flask, render_template, redirect, request, abort, send_from_directory

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kim'}
    return render_template('index.html', title='Home', user=user)


@app.route('/start') # Do I need GET or POST methods for this route?
def start():
    questions = [{
        'q': 'Which was never a train line?',
        'c1': 'J',
        'c2': 'K',
        'c3': '9'
    }]


    random_q = questions[0] # TODO: Make this random for a list longer than one item




    return render_template('start.html', title='Start Game', question=random_q['q'], choice1=random_q['c1'], choice2=random_q['c2'],
                           choice3=random_q['c3'])


# @app.route('/final')
# def end():
    # TODO: return render_template(, title='Final Score')
if __name__ == "__main__":
    app.run(debug=True)