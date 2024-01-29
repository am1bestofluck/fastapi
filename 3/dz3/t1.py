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

from flask import Flask, request, render_template, url_for

# noinspection PyUnresolvedReferences
from t1_db import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    css = url_for('static', filename="main.css")
    header = "Register to proceed"
    if request.method == "POST":
        pass

    return render_template("form.html", css_file=css,
                           header=header)
