from secrets import token_hex

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators



class LoginForm(FlaskForm):
    name_form = StringField("Name", validators=[validators.InputRequired()])
    surname_form = StringField("Surname",
                               validators=[validators.InputRequired()])
    email_form = StringField("Mail", validators=[validators.InputRequired(),
                                                 validators.Email()])
    password_form = PasswordField("Password",
                                  validators=[validators.InputRequired()])
    confirm_form = PasswordField("Confirm Password", validators=[
        validators.EqualTo('password_form')])
    agreement_form = BooleanField(
        "Agree to have my data stored, sold, misused in any ways biz sees fit.",
        validators=[validators.InputRequired()])
