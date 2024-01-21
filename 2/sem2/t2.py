"""
сделать страничку с картинкой и ссылкой на страничку для загрузки картинок
"""

from flask import Flask, render_template, make_response, request
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)


@app.route("/")
def index():
    out = make_response(render_template("t2_pic.html"))
    return out


@app.route("/upload/", methods=["GET", "POST"])
def upload_pic():
    """Это жесть :( :)"""
    pg = "t2_upload.html"
    if request.method == "POST":
        out = make_response(render_template(pg))
        pic = request.files.get("pic_")
        print(request.files)
        print(f"{pic=}")
        name = secure_filename(pic.filename)
        pic.save(PurePath.joinpath(Path.cwd(), 'upload', name))
        return out
    return render_template(pg)


if __name__ == '__main__':
    app.run()
