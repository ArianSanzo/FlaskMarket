from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    # noinspection PyMethodMayBeStatic
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist.')

    # noinspection PyMethodMayBeStatic
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exist.')

    username = StringField(label='Username: ', validators=(Length(min=3, max=30), DataRequired()))
    email_address = StringField(label='Email address: ', validators=(Length(max=50), Email(), DataRequired()))
    password1 = PasswordField(label='Password: ', validators=(Length(min=6, max=60), DataRequired()))
    password2 = PasswordField(label='Confirm password: ', validators=((EqualTo('password1')), DataRequired()))
    submit = SubmitField(label='Create Account')
