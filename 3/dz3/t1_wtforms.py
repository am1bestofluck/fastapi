from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from secrets import token_hex
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, email, DataRequired, equal_to

from t1 import app

app.config['SECRET_KEY'] = token_hex()
csrf = CSRFProtect(app)

print(app.config['SECRET_KEY'])


class LoginForm(FlaskForm):
    name_form = StringField()
    surname_form = StringField()
    email_form = StringField()
    password_form = PasswordField()
    confirm_form = PasswordField()
