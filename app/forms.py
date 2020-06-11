from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators = [DataRequired()])
    password = PasswordField('Pasword: ', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit