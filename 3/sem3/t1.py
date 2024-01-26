from flask import Flask,render_template
from t1_db import db, Students, Stream

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students_streams.db"
db.init_app(app)



@app.route("/")
def get_all():
    print("k")
    return "todo"#render_template("todo")



if __name__ == '__main__':
    app.run(port=80)