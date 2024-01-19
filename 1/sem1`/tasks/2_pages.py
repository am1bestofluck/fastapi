"""Добавляем 2 страницы
"""

from flask import Flask

app1 = Flask("__main__")


@app1.route("/about/")
def about():
    return "Hi. My name is AM"


@app1.route("/contacts/")
def contacts():
    return "I'll find You Myself in due time."


if __name__ == '__main__':
    app1.run()
