from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='Username: ', validators=(Length(min=3, max=30), DataRequired()))
    email_address = StringField(label='Email address: ', validators=(Length(max=50), Email(), DataRequired()))
    password1 = PasswordField(label='Password: ', validators=(Length(min=6, max=60), DataRequired()))
    password2 = PasswordField(label='Confirm password: ', validators=((EqualTo('password1')), DataRequired()))
    submit = SubmitField(label='Create Account')
