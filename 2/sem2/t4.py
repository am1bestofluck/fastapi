"""
принять текст, и вывести на другой странице количество слов
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("t4_main.html")


@app.post("/")
def index_post():
    text_=request.form.get("text_here")
    words=len(text_.split())
    return render_template("t4_out.html",words=words,content=text_)

if __name__ == '__main__':
    app.run()
