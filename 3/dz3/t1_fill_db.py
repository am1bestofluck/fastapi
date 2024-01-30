"""заполняем таблицу потому что так веселее"""
import random
from random import choices, choice
from string import ascii_lowercase

from t1_db import db, User, NAME_SURNAME_SIZE_CAP, MAIL_SIZE_CAP
# from t1 import app

from hashlib import md5

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
# db.init_app(app)


def _create_user(**kwargs):
    name_, surname_, mail_, password_ = kwargs['name'], kwargs['surname'], kwargs['mail'], kwargs['password']
    password_ = md5(password_.encode(encoding="UTF-8")).hexdigest()
    return User(name=name_, surname=surname_, email=mail_, password=password_)


def add_from_form(app, **kwargs):
    user = _create_user(**kwargs)
    db.session.add(user)
    db.session.commit()


LETTERS = {0: "aeiouy",
           1: "bcdfghjklmnpqrstvwz",
           2: "aeiouybcdfghjklmnpqrstvwz"}


def randomize_driver():
    global LETTERS
    first_letters = choices(LETTERS[2], k=2)
    name, surname = first_letters[0], first_letters[1]
    # генерим имя
    for i in range(max(5, choice(range(NAME_SURNAME_SIZE_CAP - 1)))):
        sample = 1 if name[-1] in LETTERS[0] else 0
        name = name + choice(LETTERS[sample])
    name = name.title()
    # генерим фамилию
    for i in range(max(5, choice(range(NAME_SURNAME_SIZE_CAP - 1)))):
        sample = 1 if surname[-1] in LETTERS[0] else 0
        surname = surname + choice(LETTERS[sample])
    surname = surname.title()
    name_size, host_size, res_size = 0, 0, 0
    while sum([name_size, host_size, res_size]) not in range(3, 30):
        name_size = choice(range(1, MAIL_SIZE_CAP))
        host_size = choice(range(1, MAIL_SIZE_CAP))
        res_size = choice(range(1, MAIL_SIZE_CAP))

    mail = ''.join(choices(LETTERS[2], k=name_size)) + \
           '@' + ''.join(choices(LETTERS[2], k=host_size)) + \
           '.' + ''.join(choices(LETTERS[2], k=res_size))

    return {'name': name, 'surname': surname, "email": mail}


# @app.cli.command("build")
# def build():
#     db.create_all()
#     print("built")
#
#
# @app.cli.command("create-db")
# def randomize():
#     for i in range(10):
#         tmp = randomize_driver()
#         print("created!")
#         user = User(**tmp)
#         db.session.add(user)
#     db.session.commit()
#     print("added!")


if __name__ == '__main__':
    # # build()
    # randomize()
    name, surname, mail, password = "asd", "aasd", "a@q.r", "qwerty"
    add_from_form(None,name=name, surname=surname, mail=mail, password=password)
