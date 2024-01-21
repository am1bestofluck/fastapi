"""
создать кнопку с переходом, с упоминанием имени
"""

from flask import Flask, render_template, make_response, request, url_for

app = Flask(__name__)


@app.route("/", methods=["post", "get"])
def index():
    if request.method == "POST":
        name = request.form.get("name_")
        return render_template("t1_redirect.html", name=name)

    out = make_response(render_template("t1_button.html"))
    return out


# @app.post("/submit/")
# def submit_name():
#     name = request.form.get("name_")
#     return render_template("t1_redirect.html", name=name)


if __name__ == '__main__':
    app.run()
