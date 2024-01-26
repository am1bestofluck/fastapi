"""
Форма должна содержать поля
  "Имя",
   "Фамилия",
    "Email",
     "Пароль"
"""

from flask_sqlalchemy import SQLAlchemy

NAME_SURNAME_SIZE_CAP = 32
PASSWORD_SIZE_CAP = 32
MAIL_SIZE_CAP = 32
db = SQLAlchemy()


class User(db.Model):
    class_hint = "User"
    global NAME_SURNAME_SIZE_CAP
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(NAME_SURNAME_SIZE_CAP), nullable=False)
    surname = db.Column(db.String(NAME_SURNAME_SIZE_CAP), nullable=False)
    email = db.Column(db.String(MAIL_SIZE_CAP), nullable=False, unique=True)
    password = db.Column(db.String(PASSWORD_SIZE_CAP))

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.surname = kwargs['surname']
        self.email = kwargs['email']
        self.password = kwargs.get('password',"")

    def __repr__(self):
        return f"{self.class_hint} {self.surname} {self.name}"


if __name__ == '__main__':
    print(User)
