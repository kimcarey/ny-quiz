from flask import render_template, redirect, request, abort, send_from_directory
from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'Kim'}
    return render_template('index.html', title='Home', user=user)

@flask_app.route('/start-game')
def start():
    user = {'username': 'Kim'}
    #TODO: return render_template(())


@flask_app.route('/final')
def end():
    user = {'username': 'Kim'}
    #TODO: return render_template()

