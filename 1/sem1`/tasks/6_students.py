"""

"""
from datetime import date
from flask import Flask, render_template
import json


class Student:
    spec = "Student"

    def __init__(self, *, name: str, surname: str, birth_year: int, avg: float):
        self.full_name = f"{name}_{surname}".title()
        self.age = date.today().year - birth_year
        self.avg = avg

    def __str__(self):
        return f"{self.spec} {self.full_name}"

    def __repr__(self):
        return str(self)

def students_to_map(a:list[Student]) -> dict:
    out = dict()
    for i in a:
        out[i.full_name] = {"age":i.age,"grade":i.avg}
    return  out

def unpack_students() -> list[Student]:
    """гребём студентов из json"""

    out = []
    with open("src/students.json") as file:
        dump = json.load(file)
        for item in dump['students']:
            out.append(
                Student(name=item['name'], birth_year=item['b.y.'], surname=item['surname'], avg=item['avg_grade']))
    return out

app = Flask(__name__)


@app.route("/students/")
def show_students():
   students= unpack_students()
   return render_template("students.html", a=students[0],b=students[1],c=students[2])

@app.route("/mapst/")
def show_as_dict():
    temp = {"AM":["AM",30,5.0],"DM":["DM",26,4.9],"SI":["SI",34,5.0],"MA":["MA",34,4.8]}
    return render_template("students2.html",**temp)


@app.route ("/dictst/")
def show_as_dict2():
    out = {"students":{i.full_name:[i.age,i.avg] for i in unpack_students()}}
    return render_template("students3.html",**out)
if __name__ == '__main__':
    app.run()