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

from flask import Flask, request, render_template, url_for
from flask_wtf.csrf import CSRFProtect

# noinspection PyUnresolvedReferences
from t1_db import db, User
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
        pass

    return render_template("form.html", css_file=css,
                           header=header, form=LoginForm())
