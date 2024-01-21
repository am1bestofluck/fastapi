"""
сделать страницу авторизации с переходом на "привет!" или ошибка 403
"""

from flask import Flask, render_template, url_for, request, abort
from string import ascii_lowercase, ascii_uppercase, digits

app = Flask(__name__)


def validate_pw(item: str):
    a, b, c = set(ascii_uppercase), set(ascii_lowercase), set(digits)
    if not a.intersection(set(item)) or \
            not b.intersection(set(item)) or \
            not c.intersection(set(item)):
        return False
    return True


@app.get("/")
def index():
    return render_template("t3_main.html")


@app.post("/")
def check_pw():
    if not validate_pw(request.form.get('pw')):
        print("notok")
        abort(403)
    return render_template("t3_hi.html")


# @app.route("/control_panel/")
# def cp():
#     return render_template("t3_hi.html")


if __name__ == '__main__':
    app.run()
