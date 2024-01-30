"""

Создать форму для регистрации пользователей на сайте.
 Форма должна содержать поля
  "Имя",
   "Фамилия",
    "Email",
     "Пароль"
      и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных,
 а пароль должен быть зашифрован.
"""

from secrets import token_hex

from flask import Flask, request, render_template, url_for, flash
from flask_wtf.csrf import CSRFProtect

# noinspection PyUnresolvedReferences
from t1_db import db, User
from t1_fill_db import add_from_form
from t1_wtforms import LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
app.config['SECRET_KEY'] = token_hex()

csrf = CSRFProtect(app)
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    css = url_for('static', filename="main.css")
    header = "Register to proceed"
    if request.method == "POST":
        add_from_form(app, name=request.form.get('name_form'), surname=request.form.get('surname_form'),
                      mail=request.form.get('email_form'), password=request.form.get('name_form'))
        flash("Nice to meet you!", category="Success")
        return render_template("paidwall.html", content="Login to continue?",
                               header="Success", css_file=css)

    return render_template("form.html", css_file=css,
                           header=header, form=LoginForm())
