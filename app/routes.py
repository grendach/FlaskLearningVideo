from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Dmytro'}
    posts = [
        {
            'author': {'username': 'Mariusz'},
            'body': 'Beautiful day in Wroclaw!'
        },
        {
            'author': {'username': 'Oleksandr'},
            'body': 'Hi from Zhdany!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)