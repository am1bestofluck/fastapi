"""выводим страничку"""

from flask import Flask,render_template

app = Flask(__name__,template_folder="templates_test")

NO_GO = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My 1st flask page</title>
</head>
<body>
    <h2>Привет-здрасьте!</h2>
</body>
</html>
"""

@app.route("/")
def index():
    return NO_GO

@app.route("/page/")
def index_template():
    return render_template("hello_title.html")

if __name__ == '__main__':
    app.run()