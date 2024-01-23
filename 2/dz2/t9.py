"""
Создать страницу,   +
на которой будет форма для ввода имени  +
и электронной почты +
При отправке которой    +
будет создан cookie файл с данными пользователя
Также будет произведено перенаправление на страницу приветствия,    +
где будет отображаться имя пользователя.    +
На странице приветствия должна быть кнопка "Выйти"  +
При нажатии на кнопку будет удален cookie файл с данными пользователя   +
 и произведено перенаправление на страницу ввода имени и электронной почты  - я щас заплачу ._.
"""

from flask import Flask, render_template, make_response, request, url_for, \
    redirect, flash
from werkzeug.datastructures import MultiDict
from markupsafe import escape

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def auth():
    args = {
        "title": "Hello?",
        "header": "Good day, dear. Care to introduce yourself?",
        "picture": url_for('static', filename='img/peach_0.png')
    }
    out = make_response(render_template("t9_login.html", **args))
    out.set_cookie("name", max_age=0)
    out.set_cookie("mail", max_age=0)
    return out


@app.post("/submit/")
def authed():
    args = {
        "mail": escape(request.form.get("mail")),
        "name": escape(request.form.get("name")).title()}
    out = make_response(render_template("t9_panel.html", **args))
    print('roll')
    for key_ in args:
        out.set_cookie(key_, args[key_])
    return out


@app.post("/logout/")
def logout():
    return redirect(url_for('auth'))


if __name__ == '__main__':
    app.run(port=80)
