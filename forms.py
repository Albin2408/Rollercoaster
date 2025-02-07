from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Form for user registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# Form for user login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# Form for adding a roller coaster
class AddCoasterForm(FlaskForm):
    park = StringField('Park', validators=[DataRequired()])
    coaster = StringField('Coaster', validators=[DataRequired()])
    submit = SubmitField('Add Coaster')

# Form for retrieving weather information
class WeatherForm(FlaskForm):
    zipcode = StringField('Zipcode', validators=[DataRequired(), Length(min=5, max=5)])
    submit = SubmitField('Get Weather')
