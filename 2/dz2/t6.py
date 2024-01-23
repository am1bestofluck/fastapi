"""
Создать страницу
на которой будет форма  +
для ввода имени ?
и возраста пользователя +
и кнопка "Отправить"    +
При нажатии на кнопку   +
будет произведена проверка возраста +
 и переход на страницу  +
  с результатом или на страницу с ошибкой
   в случае некорректного возраста.

"""

from random import randint

from flask import Flask, render_template, abort, request, url_for

from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def auth():
    return render_template("t6_base.html")


@app.post("/submit/")
def content():
    print("ok")
    name = escape(request.form.get("name")).title()
    age = int(escape(request.form.get("age")))
    if age not in range(1, 120):
        abort(400)
    if age in range(1, 19):
        abort(403)
    msg = f"Hey, {name}. Thoughts?"
    pic = url_for('static', filename=f'img/peach_{randint(0,1)}.png')
    return render_template("t6_out.html", msg=msg, pic=pic)


@app.errorhandler(400)
def err400(error_code):
    name = escape(request.form.get("name")).title()
    error_message = f"Nice try, {name.title()}"
    return render_template("t6_error.html", error_code=error_code,
                           error_message=error_message)


@app.errorhandler(403)
def err403(error_code):
    name = escape(request.form.get("name")).title()
    error_message = f"Hey {name}. Come back with parents may be?"
    return render_template("t6_error.html", error_code=error_code,
                           error_message=error_message)


if __name__ == '__main__':
    app.run()
