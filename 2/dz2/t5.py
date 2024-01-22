"""
Создать страницу,   +
 на которой будет форма +
  для ввода +
   двух чисел   +
   и выбор операции (сложение, вычитание, умножение или деление)    +
    и кнопка "Вычислить"    +
При нажатии на кнопку   +
будет произведено вычисление результата выбранной операции
и переход на страницу с результатом.    +

"""

from flask import Flask, render_template, url_for, request, abort
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("t5_ui.html")


@app.post("/submit")
def evaluated():
    a = {
        "num1": int(escape(request.form.get("fst"))),
        "num2": int(request.form.get("snd")),
        "op": request.form.get("op")
    }

    match a["op"]:
        case "*":
            a["res"] = a["num1"] * a["num2"]
        case "/":
            a["res"] = a["num1"] / a["num2"]
        case "+":
            a["res"] = a["num1"] + a["num2"]
        case "-":
            a["res"] = a["num1"] - a["num2"]
        case _:
            abort(404)

    return render_template("t5_out.html", **a)


if __name__ == '__main__':
    app.run()
