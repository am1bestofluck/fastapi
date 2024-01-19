"""написать функцию выводящую сумму чисел"""

from flask import Flask

app = Flask("__main__")


@app.route("/sum/")
def sum_(items: tuple[int] = (1, 2, 34)):
    return str(sum(items))


@app.route("/sum_<int:a>+<int:b>/")
def sum2(a: str, b: str):
    # return a+b
    return str(int(a) + int(b))


@app.route("/sumints/<int:c>/<int:d>/")
def sum_ints(c, d):
    return str(c+d)


if __name__ == '__main__':
    app.run()
