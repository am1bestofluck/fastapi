"""
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.

В таблице "Факультеты" должны быть следующие поля: id и название
факультета.


"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    group = db.Relationship("stream", back_populates='Stream.id')
    stream = db.Column(db.Integer, nullable=False)


class Stream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)


if __name__ == '__main__':
    print(Students, Stream)
