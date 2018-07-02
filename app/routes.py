from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dmytro'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Wroclaw'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Go away, you fucken assholes!'
        }
    ]
    return render_template('index.html', title='Home',  user=user, posts=posts)

